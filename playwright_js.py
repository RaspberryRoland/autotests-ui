from playwright.sync_api import sync_playwright

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN,
              wait_until='networkidle')

    new_text = 'New Text'
    page.evaluate(
        """
        (text) => {const title =
            document.getElementById('authentication-ui-course-title-text')
            title.textContent = '{text}'
        }
        """,
        new_text
    )

    page.wait_for_timeout(5000)