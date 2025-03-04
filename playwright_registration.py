from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # locators
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    register_button = page.get_by_test_id('registration-page-registration-button')

    # action
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")

    register_button.click()

    # check dashboard
    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_have_text("Dashboard")
