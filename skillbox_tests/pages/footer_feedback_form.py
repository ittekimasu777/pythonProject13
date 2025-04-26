
from selenium.webdriver.common.by import By
from .feedback_form import FeedbackForm


class FooterFeedbackForm(FeedbackForm):
    FORM = (By.CSS_SELECTOR, "footer form.feedback-form")
    NAME_INPUT = (By.CSS_SELECTOR, "footer input[name='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "footer input[name='email']")
    PHONE_INPUT = (By.CSS_SELECTOR, "footer input[name='phone']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "footer form.feedback-form button[type='submit']")
    ERROR_MESSAGES = (By.CSS_SELECTOR, "footer form.feedback-form .error-message")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "footer form.feedback-form .success-message")