from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI App"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "FastAPI application with best practices"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=True
    )

@lru_cache
def get_settings() -> Settings:
    return Settings() 