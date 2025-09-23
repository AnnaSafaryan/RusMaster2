"""
Понимание текста: логика
    Абзацы исходного текста перемешаны случайным образом,
    и необходимо восстановить логический порядок абзацев.
"""

from web.backend.data.alphabet import rus
from web.backend.helpers.utils import shuffle, sort_order, split_passes


def main(text, alphabet):
    passes = split_passes(text)
    assert len(passes) >= 3

    letters = list(alphabet.upper()[: len(passes)])
    key_letters, _ = shuffle(letters)
    task_letters, _ = shuffle(letters)
    while key_letters == task_letters:
        task_letters, _ = shuffle(letters)

    let2pas = {i: pas for i, pas in zip(key_letters, passes)}

    task = sort_order(let2pas, order=task_letters)
    keys = [(i + 1, let) for i, let in enumerate(key_letters)]

    return task, keys


if __name__ == "__main__":
    from web.backend.data.test_text import test_text

    print(main(text=test_text, alphabet=rus))
