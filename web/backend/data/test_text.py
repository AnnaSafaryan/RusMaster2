from web.backend.config import config

with open(config.TEST_TEXT_PATH, encoding="utf-8") as f:
    raw_text = f.read()
