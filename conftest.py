import pytest
from playwright.sync_api import Page

from utils.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture(scope="session")
def config() -> Config:
    return Config()


@pytest.fixture(scope="session")
def base_url(config: Config) -> str:
    return config.base_url


@pytest.fixture(autouse=True)
def log_test_start(request):
    logger.info("Starting test: %s", request.node.name)
    yield
    logger.info("Finished test: %s", request.node.name)


@pytest.fixture
def authenticated_page(page: Page, config: Config) -> Page:
    """Example login fixture — update selectors for your app."""
    page.goto(f"{config.base_url}/login")
    page.get_by_label("Email").fill(config.username)
    page.get_by_label("Password").fill(config.password)
    page.get_by_role("button", name="Log in").click()
    return page


import pytest

from api.api_client import ApiClient
from utils.config import Config

@pytest.fixture
def api_client():
    config = Config()
    config.api_base_url = "https://jsonplaceholder.typicode.com"

    client = ApiClient(config)

    yield client

    client.session.close()