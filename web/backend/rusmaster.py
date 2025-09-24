import pickle

import ru_core_news_sm

from web.backend.config import config
from web.backend.data.alphabet import rus
from web.backend.helpers.preprocessing import preprocess
from web.backend.helpers.utils import create_path, generate_id, read_file

file_path = config.DATA_DIR / "texts" / "test_text_2.txt"
file_id = generate_id(file_path)
temp_path = config.TEMP_DIR / f"{file_id}"
preprocessed_path = temp_path / "preprocessed.pkl"
create_path(temp_path)

nlp = ru_core_news_sm.load()
# TODO: forced
if preprocessed_path.exists():
    print(f"Loadig {preprocessed_path}")
    with preprocessed_path.open("rb") as file:
        preprocessed = pickle.load(file)
else:
    print(f"Processing {preprocessed_path}")
    text = read_file(file_path)
    preprocessed = preprocess(text=text, spacy_model=nlp)
    with preprocessed_path.open("wb") as file:
        pickle.dump(obj=preprocessed, file=file)


if __name__ == "__main__":
    # from web.backend.exercises.one import main as one
    from web.backend.exercises.two import main as two

    # from web.backend.exercises.three import main as three
    # task, keys = one(alphabet=rus, n_chunks=10, chunksize=1)
    task, keys = two(preprocessed.text, alphabet=rus)

    print(task, keys)
