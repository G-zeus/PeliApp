from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    TMDB_API_URL: str
    TMDB_AUTH_TOKEN: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
