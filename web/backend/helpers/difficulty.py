import json

from web.backend.config import config

lexmin_path = config.DATA_DIR / "lexmin"
dict_path = lexmin_path / "lexmins.json"

lexmins = json.load(fp=open(dict_path, encoding="utf-8"))
# print(lexmins)


def in_min(word, level):
    """
    Проверяет, есть ли слово в минимуме уровня
    """
    if word.lower() in lexmins.get(level):
        return True
    else:
        return False


def level_sent(sentence, level, threshold=0.8):
    """
    Считает отношение слов из минимума ко всем значимым словам в предложении
    """
    meaningful_words = [
        token
        for token in sentence
        if token.alpha and not token.stop_word and token.text != "\n"
    ]
    if meaningful_words:  # если набрались знаменательные слова
        known_words = [token for token in meaningful_words if in_min(token.lem, level)]
        coef = len(known_words) / len(meaningful_words)
    return coef


# ПРОВЕРЯТЬ IF С ИНДЕКСАЦИЕЙ, fun.coef_sent(sent, 'B2')[0] --
# иначе всегда True, т.к. возвращает кортеж
def coef_sent(sentence, level, threshold=80):
    threshold = threshold / 100  # переводим процент в десятичное
    meaningful = [
        token
        for token in sentence
        if token.alpha and not token.stop_word and token.text != "\n"
    ]
    if meaningful:  # если набрались знаменательные слова
        known = [token for token in meaningful if in_min(token.lem, level)]
        # print(text_tokens(meaningful)) # значимые слова
        # print(text_tokens(known)) # слова из минимума
        coef = len(known) / len(meaningful)
        if coef >= threshold:
            return True, coef
        else:
            return False, coef
    else:
        coef = 0
        return False, coef


# def get_level(text):
#
#
#
# if __name__ == "__main__":
#     from web.backend.data.test_text import test_text
