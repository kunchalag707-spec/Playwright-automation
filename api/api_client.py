import requests

from utils.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class ApiClient:
    def __init__(self, config: Config | None = None):
        self.config = config or Config()
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get(self, path: str, **kwargs) -> requests.Response:
        url = f"{self.config.api_base_url.rstrip('/')}/{path.lstrip('/')}"
        logger.info("GET %s", url)
        return self.session.get(url, timeout=30, **kwargs)

    def post(self, path: str, json: dict | None = None, **kwargs) -> requests.Response:
        url = f"{self.config.api_base_url.rstrip('/')}/{path.lstrip('/')}"
        logger.info("POST %s", url)
        return self.session.post(url, json=json, timeout=30, **kwargs)

    def health(self) -> requests.Response:
        return self.get("/health")
