from web.backend.config import config
import json

lexmins = {}
lexmin_path = config.DATA_DIR / 'lexmin'
dict_path = lexmin_path / 'lexmins.json'
level_paths = lexmin_path.glob("*.txt")


for level_path in level_paths:
    level = level_path.stem
    with level_path.open(encoding='utf-8') as file:
        words = file.read().strip().lower().splitlines()
        lexmins[level] = words

json.dump(obj=lexmins, fp=open(dict_path, 'w', encoding='utf-8'),
          indent=4, ensure_ascii=False)



# def get_level(text):
#
#
#
# if __name__ == "__main__":
#     from web.backend.data.test_text import test_text
