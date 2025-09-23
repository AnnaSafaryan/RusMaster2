import locale
from random import shuffle as rnd_shuffle

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")


def split_passes(text):
    return [pas.strip() for pas in text.strip().split("\n")]


def shuffle(elements):
    shuffled = elements.copy()
    rnd_shuffle(shuffled)

    while shuffled == elements:  # защита от случайного повторения исходного порядка
        shuffled, elements = shuffle(elements)

    return shuffled, elements


def sort_alphabetic(sequence, reverse=False):
    """
    Приводит в порядок сортировку и букву Ё
    """
    return sorted(
        sequence,
        key=locale.strxfrm,
        reverse=reverse,
    )  # только для строк


def sort_order(sequence, order):
    """
    Сортирует словари (ключи) и списки кортежей из двух элементов (первый элемент)
    по заданному порядку
    """
    if isinstance(sequence, dict):
        keys = list(sequence.keys())
    elif isinstance(sequence, list):
        keys = [elem[0] for elem in sequence]
        # будем работать со словарями -- буквы или цифры всё равно не будут повторяться
        sequence = dict(sequence)
    else:
        raise ValueError

    assert keys != order

    return {elem: sequence[elem] for elem in order}


def convert_encoding(file, encoding="utf-8"):
    s = open(file, "r").read().encode(encoding, errors="backslashreplace")
    with open(file, "wb") as f:
        f.write(s)


def read_file(file):
    try:
        with open(file, encoding="utf-8") as f:
            data = f.read().strip()
    except UnicodeError:
        convert_encoding(file)
        data = read_file(file)

    return data


def resolve_paths():
    pass
