from web.backend.config import config
from web.backend.helpers.preprocessing import get_preprocessed
from web.backend.helpers.utils import create_path, generate_id


def main(file_path):
    file_id = generate_id(file_path)
    temp_path = config.TEMP_DIR / f"{file_id}"
    preprocessed_path = temp_path / config.PREPROCESSED_NAME
    create_path(temp_path)
    preprocessed = get_preprocessed(preprocessed_path)
    return preprocessed


if __name__ == "__main__":
    # from web.backend.exercises.one import main as one
    from web.backend.exercises.two import main as two
    from web.backend.helpers.loaders import json_load

    # from web.backend.exercises.three import main as three
    alphabets = json_load(config.ALPHABET_DICT)

    # file_path = config.DATA_DIR / "texts" / "test_text_2.txt"
    file_path = config.TEST_TEXT_PATH
    preprocessed = main(file_path)

    # task, keys = one(alphabet=alphabets['rus'], n_chunks=10, chunksize=1)
    task, keys = two(preprocessed.text, alphabet=alphabets["rus"])

    print(task, keys)
