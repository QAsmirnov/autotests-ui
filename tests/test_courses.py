from playwright.sync_api import sync_playwright, expect


def test_empty_course_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

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

        # save context
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # locators
        toolbar_title_text = page.get_by_test_id('courses-list-toolbar-title-text')
        folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
        view_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
        description_text = page.get_by_test_id('courses-list-empty-view-description-text')

        # check text
        expect(toolbar_title_text).to_have_text("Courses")
        expect(view_title_text).to_have_text("There is no results")
        expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")

        # check icon
        expect(folder_icon).to_be_visible()
