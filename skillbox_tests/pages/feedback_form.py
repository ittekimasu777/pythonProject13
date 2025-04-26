
from selenium.webdriver.common.by import By
from .base_page import BasePage


class FeedbackForm(BasePage):
    FORM = (By.CSS_SELECTOR, "form.feedback-form")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form.feedback-form button[type='submit']")
    ERROR_MESSAGES = (By.CSS_SELECTOR, "form.feedback-form .error-message")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "form.feedback-form .success-message")

    def fill_form(self, name=None, email=None, phone=None):
        if name:
            self.send_keys(self.NAME_INPUT, name)
        if email:
            self.send_keys(self.EMAIL_INPUT, email)
        if phone:
            self.send_keys(self.PHONE_INPUT, phone)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_error_messages(self):
        return [el.text for el in self.find_elements(self.ERROR_MESSAGES)]

    def is_success_message_displayed(self):
        return self.find_element(self.SUCCESS_MESSAGE).is_displayed()

    def is_form_displayed(self):
        return self.find_element(self.FORM).is_displayed()