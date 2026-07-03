"""Application settings and configuration management."""

import os
from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    openai_api_key: str = Field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY", ""),
        description="OpenAI API key for LLM operations"
    )

    model_name: str = Field(
        default="gpt-4o-mini",
        description="OpenAI model to use"
    )

    temperature: float = Field(
        default=0.0,
        description="Temperature for LLM responses"
    )

    max_tokens: int = Field(
        default=1000,
        description="Maximum tokens for LLM responses"
    )

    log_level: str = Field(
        default="INFO",
        description="Logging level"
    )

    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Returns:
        Settings: Application settings
    """
    return Settings()