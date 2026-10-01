import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    base_url: str = os.getenv("BASE_URL", "https://avplat-local.web.app")
    username: str = os.getenv("APP_USERNAME", "")
    password: str = os.getenv("APP_PASSWORD", "")
    api_base_url: str = os.getenv("API_BASE_URL", "")
    timeout_ms: int = int(os.getenv("TIMEOUT_MS", "30000"))
