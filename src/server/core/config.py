from typing import Literal
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    host: str = "localhost"
    port: int = 8000
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = False


config = Config()
