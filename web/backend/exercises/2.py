"""
2. Понимание текста: логика
	Абзацы исходного текста перемешаны случайным образом, и необходимо восстановить логический порядок абзацев.
"""
# TODO: можно сделать логичнее
# TODO: переписать сортировку
from random import shuffle
from web.backend.data.alphabet import rus
from web.backend.data.test_text import test_text
from web.backend.helpers.preprocessing import true_sort,  split_passes


def two(alphabet, text):
    passes = split_passes(text)
    letters = list(alphabet.upper()[:len(passes)])
    shuffle(letters)

    i_let_pas = {i + 1: pair for i, pair in
                 enumerate(zip(letters, passes))}
    print(i_let_pas, '\n')

    questions = sorted(i_let_pas.values())
    answers = [(i, i_let_pas[i][0]) for i in i_let_pas]

    return questions, answers

print(two(alphabet=rus, text=test_text))
