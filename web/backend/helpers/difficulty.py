from web.backend.config import config
from web.backend.helpers.loaders import json_load

lexmins = json_load(path=config.LEXMINS_DICT)


def level_sent(sentence, level):
    """
    Считает отношение слов из минимума ко всем значимым словам в предложении
    """
    coef = 0
    meaningful_words = sentence.meaningful_list
    if meaningful_words:
        known_words = [token for token in meaningful_words if level in token.levels]
        coef = len(known_words) / len(meaningful_words)
    return coef
