"""
Понимание текста: логика
    Абзацы исходного текста перемешаны случайным образом,
    и необходимо восстановить логический порядок абзацев.
"""

from web.backend.helpers.utils import shuffle_recursive, sort_order, split_paragraphs


def main(raw_text, alphabet):
    paragraphs = split_paragraphs(raw_text)
    assert len(paragraphs) >= 3

    letters = list(alphabet.upper()[: len(paragraphs)])
    key_letters, _ = shuffle_recursive(letters)
    task_letters, _ = shuffle_recursive(letters)
    while key_letters == task_letters:
        task_letters, _ = shuffle_recursive(letters)

    let2pas = {i: pas for i, pas in zip(key_letters, paragraphs)}

    task = sort_order(let2pas, order=task_letters)
    keys = [(i + 1, let) for i, let in enumerate(key_letters)]

    return task, keys


if __name__ == "__main__":
    from web.backend.config import config
    from web.backend.data.test_text import raw_text
    from web.backend.helpers.loaders import json_load

    alphabets = json_load(config.ALPHABET_DICT)
    task, keys = main(raw_text=raw_text, alphabet=alphabets["rus"])
    print(task, keys, sep=f"\n{'-'*30}\n")
