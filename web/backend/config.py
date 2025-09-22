from pathlib import Path

from pydantic_settings import BaseSettings

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


class PipelineSettings(BaseSettings):
    PROJECT_NAME: str = "RusMaster"

    # Paths
    DATA_DIR: Path = ROOT_DIR / "data"
    WEB_DIR: Path = ROOT_DIR / "web"
    BACKEND_DIR: Path = WEB_DIR / "backend"

    class Config:
        env_file = ROOT_DIR / ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


config = PipelineSettings()
