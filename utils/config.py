import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    base_url: str = os.getenv("BASE_URL", "https://example.com")
    username: str = os.getenv("USERNAME", "test.user@example.com")
    password: str = os.getenv("PASSWORD", "ChangeMe123!")
    api_base_url: str = os.getenv("API_BASE_URL", "https://api.example.com")
    timeout_ms: int = int(os.getenv("TIMEOUT_MS", "30000"))
