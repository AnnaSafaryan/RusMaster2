from web.backend.config import config


lexmins = {}
lexmin_path = config.DATA_DIR / 'lexmin'
level_paths = lexmin_path.glob("*.txt")

for level_path in level_paths:
    level = level_path.stem
    with level_path.open(encoding='utf-8') as file:
        words = file.read().strip().splitlines()
        lexmins[level] = words

print(lexmins)



# mins = {}
# for level in levels:
#     min = open("data\\{}.txt".format(level), encoding='utf-8').read().lower().split('\n') # получаем список слов
#     mins[level] = set(min)
#
# def get_level(text):
#
#
#
# if __name__ == "__main__":
#     from web.backend.data.test_text import test_text
