from playwright.sync_api import sync_playwright

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for character in 'user@gmail.com':
        page.keyboard.press(character, delay=300)

    page.keyboard.press('ControlOrMeta+A')

    page.wait_for_timeout(5000)