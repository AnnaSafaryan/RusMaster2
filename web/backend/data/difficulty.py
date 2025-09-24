import json

from web.backend.config import config

lexmins = {}
lexmin_path = config.DATA_DIR / "lexmin"
dict_path = lexmin_path / "lexmins.json"
level_paths = lexmin_path.glob("*.txt")


for level_path in level_paths:
    level = level_path.stem
    with level_path.open(encoding="utf-8") as file:
        words = file.read().strip().lower().splitlines()
        lexmins[level] = list(set(words))  # Object of type set is not JSON serializable

json.dump(
    obj=lexmins,
    fp=open(dict_path, "w", encoding="utf-8"),
    indent=4,
    ensure_ascii=False,
)
