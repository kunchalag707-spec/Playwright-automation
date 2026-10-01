from ast import And
from pytest_bdd import scenarios, given, when, then
scenarios("../../features/login.feature")
from pages.login_page import LoginPage
@given("I am on the login page")
def open_login_page(page):
    login_page = LoginPage(page)
    login_page.goto("https://avplat-local.web.app")

@when("I login with valid username and password")
def login_with_valid_credentials(page, config):
    login_page = LoginPage(page)
    login_page.login(
        config.username,
        config.password
    )



