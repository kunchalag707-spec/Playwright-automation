import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.test_data import  VALID_USER


@pytest.mark.login
@pytest.mark.smoke
def test_login_with_valid_credentials(page: Page, base_url: str):
    login = LoginPage(page)
    login.goto("https://avplat-local.web.app")
    login.login(VALID_USER["email"], VALID_USER["password"])

    expect(page).not_to_have_url("**/login")



