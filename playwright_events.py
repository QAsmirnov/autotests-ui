from playwright.sync_api import sync_playwright, Request, Response


def log_request(request: Request):
    print(f'request:{request.url} {request.frame}')


def log_response(response: Response):
    print(f'response:{response.url} {response.status}')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.on('request', log_request)
    page.on('response', log_response)

    page.wait_for_timeout(5000)