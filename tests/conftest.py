import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    page.get_by_test_id('registration-form-email-input').locator('input').fill("user.name@gmail.com")
    page.get_by_test_id('registration-form-username-input').locator('input').fill("username")
    page.get_by_test_id('registration-form-password-input').locator('input').fill("password")
    page.get_by_test_id('registration-page-registration-button').click()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    browser.close()
