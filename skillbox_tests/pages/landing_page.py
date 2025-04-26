from selenium.webdriver.common.by import By
from .base_page import BasePage
from .search_component import SearchComponent


class LandingPage(BasePage):
    ALL_COURSES_BUTTON = (By.LINK_TEXT, "Все курсы")

    def __init__(self, driver):
        super().__init__(driver)
        self.search = SearchComponent(driver)

    def open_all_courses(self):
        self.click(self.ALL_COURSES_BUTTON)
        return self