import hashlib
import locale
from os import makedirs
from random import shuffle as rnd_shuffle

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")


def split_paragraphs(text):
    return [paragraph.strip() for paragraph in text.strip().split("\n")]


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
    )  # TODO: пока только для строк


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
    """
    Читает из файла, преобразует кодировку,
    убирает двойные пробелы и ручные переносы
    """
    try:
        with open(file, encoding="utf-8") as f:
            text = f.read().strip()
            while "  " in text:
                text = text.replace("  ", " ")
            text = text.replace("-\n", "")
    except UnicodeError:
        convert_encoding(file)
        text = read_file(file)

    return text


def generate_id(file_path, data="content"):
    """
    Хэш по содержимому файла (по умолчанию) или пути к нему
    """
    if data == "content":
        h = hashlib.md5(file_path.read_bytes())
    elif data == "path":
        h = hashlib.md5(str(file_path).encode("utf-8"))
    else:
        raise ValueError
    return h.hexdigest()


def resolve_paths():
    pass


def create_path(path):
    """
    Создаёт указанную директорию
    """
    if path.exists():
        print(f"{path} exists.")
    else:
        makedirs(path)
        print(f"{path} created.")
