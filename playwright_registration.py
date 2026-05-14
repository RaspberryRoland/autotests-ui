from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    #page = browser.new_page()
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")


    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')

    dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_header).to_be_visible()
    expect(dashboard_header).to_have_text('Dashboard')

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(5000)