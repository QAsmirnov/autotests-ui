from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # locators
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    register_button = page.get_by_test_id('registration-page-registration-button')

    # check button is not active
    expect(register_button).not_to_be_enabled()

    # input
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")

    # check button is active
    expect(register_button).to_be_enabled()
