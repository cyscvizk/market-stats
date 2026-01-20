from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Config(BaseSettings):
    host: str = "localhost"
    port: int = 8000
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    google_api_key: str = ""

    @field_validator('google_api_key')
    @classmethod
    def validate_api_key(cls, v):
        if not v or v == "":
            raise ValueError("GOOGLE_API_KEY must be set in .env file")
        return v

    class Config:
        env_file = ".env"
        case_sensitive = False


config = Config()
