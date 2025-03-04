from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)

    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill('smirnov.kz1@yandex.ru')

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill('pass1232')

    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    worng_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')

    expect(worng_email_or_password_alert).to_be_visible()
    expect(worng_email_or_password_alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(5000)
