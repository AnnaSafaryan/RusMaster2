import locale

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")


def true_sort(sequence, reverse=False):
    # return sorted(sequence, key=locale.strxfrm, reverse=reverse) # только для строк
    pass


def split_passes(text):
    return [pas.strip() for pas in text.strip().split("\n")]
