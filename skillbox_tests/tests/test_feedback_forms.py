import pytest
from pages.landing_page import LandingPage
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def landing_page(browser):
    browser.get("https://skillbox.ru/")
    return LandingPage(browser)


def test_feedback_form_validation(landing_page):

    test_cases = [
        {"name": "", "email": "test@example.com", "phone": "+79991112233", "expected_error": "Обязательное поле"},
        {"name": "Test", "email": "invalid-email", "phone": "+79991112233", "expected_error": "Некорректный email"},
        {"name": "Test", "email": "test@example.com", "phone": "123", "expected_error": "Некорректный телефон"},
    ]

    for case in test_cases:
        landing_page.feedback_form.fill_form(case["name"], case["email"], case["phone"])
        landing_page.feedback_form.submit()

        errors = landing_page.feedback_form.get_error_messages()
        assert case["expected_error"] in errors, f"Expected error '{case['expected_error']}' not found in {errors}"

        assert landing_page.feedback_form.is_form_displayed(), "Form should remain visible after invalid submission"


def test_footer_feedback_form_validation(landing_page):

    test_cases = [
        {"name": "", "email": "test@example.com", "phone": "+79991112233", "expected_error": "Обязательное поле"},
        {"name": "Test", "email": "invalid-email", "phone": "+79991112233", "expected_error": "Некорректный email"},
    ]

    for case in test_cases:
        landing_page.footer_feedback_form.fill_form(case["name"], case["email"], case["phone"])
        landing_page.footer_feedback_form.submit()

        errors = landing_page.footer_feedback_form.get_error_messages()
        assert case["expected_error"] in errors, f"Expected error '{case['expected_error']}' not found in {errors}"

        assert landing_page.footer_feedback_form.is_form_displayed(), "Form should remain visible after invalid submission"


def test_successful_feedback_submission(landing_page):

    landing_page.feedback_form.fill_form(
        name="Test User",
        email="test@example.com",
        phone="+79991112233"
    )
    landing_page.feedback_form.submit()

    assert landing_page.feedback_form.is_success_message_displayed(), "Success message should be displayed"
    assert not landing_page.feedback_form.is_form_displayed(), "Form should disappear after successful submission"


def test_successful_footer_feedback_submission(landing_page):

    landing_page.footer_feedback_form.fill_form(
        name="Test User",
        email="test@example.com",
        phone="+79991112233"
    )
    landing_page.footer_feedback_form.submit()

    assert landing_page.footer_feedback_form.is_success_message_displayed(), "Success message should be displayed"
    assert not landing_page.footer_feedback_form.is_form_displayed(), "Form should disappear after successful submission"