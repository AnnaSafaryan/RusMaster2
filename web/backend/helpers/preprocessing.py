# import spacy
import ru_core_news_sm

nlp = ru_core_news_sm.load()


def preprocess(text):
    doc = nlp(text)

    for sent in doc.sents:
        print(sent)


if __name__ == "__main__":
    from web.backend.data.test_text import test_text

    preprocess(text=test_text)
