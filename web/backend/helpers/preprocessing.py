from itertools import chain

import spacy

from web.backend.helpers.difficulty import lexmins

# TODO: добавлять и переопределять в оригинальных классах, а не писать новые


class Token:
    def __init__(self, token):
        assert isinstance(token, spacy.tokens.token.Token)
        self.original = token
        self.text = token.text  # сам токен
        self.norm = token.norm_  # нормализованный токен
        self.lem = token.lemma_  # лемма
        self.pos = (token.pos_, token.tag_)  # часть речи
        self.morph_dict = token.morph.to_dict()  # грамм. разбор в виде словаря
        self.syntax = token.dep_  # синтакс. роль
        self.is_digit = token.is_digit  # число ли
        self.is_alpha = token.is_alpha  # буквы ли
        self.is_stop = token.is_stop  # стоп-слово ли
        self.is_title = token.is_title  # начинается ли с заглавной
        self.is_punct = token.is_punct  # знак препинания
        self.idx_text = token.i  # номер в тексте
        # TODO: предлоги и местоимения -- тоже по лекс минимумам?
        self.is_meaningful = True if self.is_alpha and not self.is_stop else False
        self.levels = [
            level
            for level in lexmins
            if self.is_meaningful and self.lem in lexmins[level]
        ]
        self.len = len(token)  # длина токена
        self.idx_sent = None  # номер в предложении
        del self.original

    def __repr__(self):
        return f"{Token.__name__}({vars(self)!r})"


class Sentence:
    def __init__(self, sentence):
        assert isinstance(sentence, spacy.tokens.span.Span)
        self.original = sentence
        self.text = sentence.text
        self.tokens = [Token(token) for token in list(self.original)]
        self.meaningful_list = [token for token in self.tokens if token.is_meaningful]
        self.difficulty = 0  # TODO
        self.idx_text = 0  # TODO
        del self.original

    def __repr__(self):
        return f"{Sentence.__name__}({vars(self)!r})"


class Document:
    def __init__(self, document):
        assert isinstance(document, spacy.tokens.doc.Doc)
        self.original = document
        self.text = self.original.text
        self.sentences = [Sentence(sentence) for sentence in self.original.sents]
        self.tokens = list(chain(self.sentences))
        self.paragraphs = []  # TODO
        self.meaningful_list = list(
            chain(
                [sentence.meaningful_list for sentence in self.sentences],
            ),
        )
        self.difficulty = sum([sentence.difficulty for sentence in self.sentences]) / len(
            self.sentences,
        )  # средняя сложность текста
        del self.original

    def __repr__(self):
        return f"{Document.__name__}({vars(self)!r})"


def preprocess(text, spacy_model):
    doc = spacy_model(text)
    return Document(document=doc)


if __name__ == "__main__":
    import ru_core_news_sm

    from web.backend.data.test_text import text

    nlp = ru_core_news_sm.load()
    preprocessed = nlp(text)
    # print(type(preprocessed))
    # print(list(preprocessed.tokens))
    preprocessed = Document(preprocessed, spacy_model=nlp)
    # print(preprocessed)
    # print(list(preprocessed))
    # print(Token(preprocessed[7]).__repr__())
    # print(Token(preprocessed[1]).__repr__())
    # print(Token(preprocessed[-1]).__repr__())
