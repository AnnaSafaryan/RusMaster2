import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
words = ["яблоко", "ёж", "арбуз", "ёлка", "банан"]
words = [(i, word) for i, word in enumerate(words)]
print(sorted(words, key=locale.strxfrm))
print(sorted(words))

