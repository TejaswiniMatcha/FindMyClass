import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

from pydantic import BaseModel, Field, validator


root_dir = Path(__file__).resolve().parents[2]
if load_dotenv is not None:
    load_dotenv(root_dir / ".env")


STATIC_DIR = str(root_dir / "static")


def _parse_cors_origins(value):
    if value is None:
        return ["http://127.0.0.1:5173", "http://localhost:5173"]
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return value


class Settings(BaseModel):
    app_name: str = "FindMyClass"
    environment: str = "development"
    debug: bool = False

    database_url: str = Field(default="postgresql://postgres:2219@localhost:5432/findmyclass")
    cors_origins: list[str] = Field(default_factory=lambda: ["http://127.0.0.1:5173", "http://localhost:5173"])
    static_dir: str = "static"
    default_search_limit: int = 20

    @validator("cors_origins", pre=True)
    def parse_cors_origins(cls, value):
        return _parse_cors_origins(value)

    @validator("default_search_limit", pre=True)
    def parse_default_search_limit(cls, value):
        return int(value) if value is not None else 20


settings = Settings(
    app_name=os.getenv("APP_NAME", "FindMyClass"),
    environment=os.getenv("ENVIRONMENT", "development"),
    debug=os.getenv("DEBUG", "false").lower() in ("1", "true", "yes"),
    database_url=os.getenv("DATABASE_URL", "postgresql://postgres:2219@localhost:5432/findmyclass"),
    cors_origins=_parse_cors_origins(os.getenv("CORS_ORIGINS")),
    static_dir=os.getenv("STATIC_DIR", STATIC_DIR),
    default_search_limit=os.getenv("DEFAULT_SEARCH_LIMIT", 20),
)
