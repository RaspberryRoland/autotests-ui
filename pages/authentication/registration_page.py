from playwright.sync_api import Page

from components.authentication.registration_form_component import \
    RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(page)
        self.login_link = Link(page, 'registration-page-login-link', 'Login')
        self.registration_button = Button(page,
                                          'registration-page-registration-button',
                                          'Registration')

    def fill_registration_form(self, email, username, password):
        self.registration_form_component.fill(email, username, password)
        self.registration_form_component.check_visible(email, username,
                                                       password)

    def click_registration_button(self):
        self.registration_button.click()
