from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    #page = browser.new_page()
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)


    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path=settings.browser_state_file)

    dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_header).to_be_visible()
    expect(dashboard_header).to_have_text('Dashboard')

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=settings.headless)
    context = browser.new_context(storage_state=settings.browser_state_file)
    page = context.new_page()

    page.goto(AppRoute.DASHBOARD)

    page.wait_for_timeout(5000)