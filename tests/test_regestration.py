from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # locators
    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    register_button = chromium_page.get_by_test_id('registration-page-registration-button')

    # action
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")
    register_button.click()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
