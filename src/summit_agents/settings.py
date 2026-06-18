from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    openai_api_key: str | None = None
    openai_model: str = "gpt-5.5"
    app_name: str = "summit-agents-sdk-starter"
    prompts_dir: Path = BASE_DIR / "prompts"
    data_dir: Path = BASE_DIR / "data"
    tracing_enabled: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
