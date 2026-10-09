
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
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



@then("I should be redirected to the trips page")
def verify_trips_page(page):

    expect(page).to_have_url(
        "https://avplat-local.web.app/trips",
        timeout=9000
    )







