from pathlib import Path

from pydantic_settings import BaseSettings

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


class PipelineSettings(BaseSettings):
    PROJECT_NAME: str = "RusMaster"

    # PATHS
    DATA_DIR: Path = ROOT_DIR / "data"
    WEB_DIR: Path = ROOT_DIR / "web"
    BACKEND_DIR: Path = WEB_DIR / "backend"
    TEMP_DIR: Path = BACKEND_DIR / "temp"

    # LINGUISTICS
    ALPHABET_DIR: Path = DATA_DIR / "alphabets"
    ALPHABET_DICT: Path = ALPHABET_DIR / "alphabets.json"

    LEXMINS_DIR: Path = DATA_DIR / "lexmins"
    LEXMINS_DICT: Path = LEXMINS_DIR / "lexmins.json"

    PREPROCESSED_NAME: str = "preprocessed.pkl"

    # DEFAULT
    TEST_TEXT_PATH: Path = DATA_DIR / "texts" / "test_text_2.txt"

    class Config:
        env_file = ROOT_DIR / ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


config = PipelineSettings()
