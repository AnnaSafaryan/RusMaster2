"""
1. Знание алфавита
	В этом задании не понадобится текст - надо просто расставить все буквы русского алфавита в правильном порядке.
"""

from web.backend.data.alphabet import rus
from random import shuffle


def one(alphabet, chunksize=1):
    alphabet = alphabet.upper()
    chunks = [alphabet[idx: idx + chunksize]
              for idx in range(0, len(alphabet), chunksize)]

    shuffled = chunks.copy()
    shuffle(shuffled)
    return shuffled, chunks

if "__main__":
    print(one(alphabet=rus, chunksize=1))