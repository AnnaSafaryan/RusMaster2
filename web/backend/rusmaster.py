# from web.backend.exercises.three import main as three
from web.backend.config import config

# from web.backend.exercises.one import main as one
# from web.backend.exercises.two import main as two
from web.backend.helpers.preprocessing import preprocess
from web.backend.helpers.utils import read_file

# from pickle import dump as pdump

file_path = config.WEB_DIR / "static" / "texts" / "test_text_1.txt"

text = read_file(file_path)

preprocesed = preprocess(text)
