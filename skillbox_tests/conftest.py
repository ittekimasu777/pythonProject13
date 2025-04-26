import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def browser():

    logger.info("Инициализация браузера Chrome")
    service = Service(ChromeDriverManager().install())
    driver = Chrome(service=service)
    driver.maximize_window()

    yield driver

    logger.info("Закрытие браузера")
    driver.quit()


@pytest.fixture
def chrome_options(chrome_options):

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    return chrome_options


@pytest.fixture(scope="session")
def base_url():

    return "https://skillbox.ru"


@pytest.fixture
def landing_page(browser, base_url):

    from pages.landing_page import LandingPage
    browser.get(base_url)
    return LandingPage(browser)


def pytest_runtest_makereport(item, call):

    if call.when == 'call' and call.excinfo is not None:
        try:
            browser = item.funcargs['browser']
            screenshot_path = f"screenshots/{item.name}.png"
            browser.save_screenshot(screenshot_path)
            logger.error(f"Тест упал, скриншот сохранен: {screenshot_path}")
        except Exception as e:
            logger.error(f"Ошибка при создании скриншота: {e}")