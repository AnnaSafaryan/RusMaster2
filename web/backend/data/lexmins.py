if __name__ == "__main__":
    from web.backend.config import config
    from web.backend.helpers.loaders import json_dump

    lexmins = {}

    for level_path in config.LEXMINS_DIR.glob("*.txt"):
        level = level_path.stem
        with level_path.open(encoding="utf-8") as file:
            words = file.read().strip().lower().splitlines()
            lexmins[level] = list(
                set(words),
            )  # Object of type set is not JSON serializable

    json_dump(data=lexmins, path=config.LEXMINS_DICT)
