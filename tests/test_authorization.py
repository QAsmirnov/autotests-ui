from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    expect(email_input).to_be_visible()

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    expect(password_input).to_be_visible()

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    email_input.fill("user.name@gmail.com")
    password_input.fill("password")

    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

