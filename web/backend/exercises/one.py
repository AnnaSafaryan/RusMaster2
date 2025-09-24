"""
Знание алфавита
    В этом задании не понадобится текст - надо просто расставить буквы
    (или сочетания букв) русского алфавита в правильном порядке.
"""

from random import sample

from web.backend.helpers.utils import shuffle_recursive, sort_alphabetic


def main(alphabet, n_chunks, chunksize):
    assert n_chunks * chunksize < len(alphabet)

    alphabet = alphabet.upper()

    chunks_all = [
        alphabet[idx : idx + chunksize] for idx in range(0, len(alphabet), chunksize)
    ]
    chunks_chosen = sample(chunks_all, n_chunks)

    task_chunks, _ = shuffle_recursive(chunks_chosen)
    key_chunks = sort_alphabetic(task_chunks.copy())

    return task_chunks, key_chunks


if __name__ == "__main__":
    from web.backend.config import config
    from web.backend.helpers.loaders import json_load

    alphabets = json_load(config.ALPHABET_DICT)
    task, keys = main(alphabet=alphabets["rus"], n_chunks=10, chunksize=2)
    print(task, keys, sep=f"\n{'-'*30}\n")
