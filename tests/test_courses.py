import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_course_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    toolbar_title_text = page.get_by_test_id('courses-list-toolbar-title-text')
    folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
    view_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
    description_text = page.get_by_test_id('courses-list-empty-view-description-text')

    expect(toolbar_title_text).to_have_text("Courses")
    expect(view_title_text).to_have_text("There is no results")
    expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")
    expect(folder_icon).to_be_visible()
