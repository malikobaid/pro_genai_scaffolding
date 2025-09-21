import os

from pydantic import BaseModel


class Settings(BaseModel):
    env: str = os.getenv("ENV", "local")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    model_default: str = os.getenv("MODEL_DEFAULT", "gpt-5-mini")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
