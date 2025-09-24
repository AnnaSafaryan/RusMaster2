if __name__ == "__main__":
    from web.backend.config import config
    from web.backend.helpers.loaders import json_dump

    alphabets = {}

    for alphabet_path in config.ALPHABET_DIR.glob("*.txt"):
        alphabet = alphabet_path.stem
        with alphabet_path.open(encoding="utf-8") as file:
            letters = file.read().strip().lower().replace("\n", "")
            # TODO: для сложной сортировки
            order = {let: i for i, let in enumerate(letters)}
            # Object of type set is not JSON serializable
            alphabets[alphabet] = letters

    json_dump(data=alphabets, path=config.ALPHABET_DICT)
