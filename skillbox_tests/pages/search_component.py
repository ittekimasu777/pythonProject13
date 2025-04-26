from selenium.webdriver.common.by import By
from urllib.parse import unquote


class SearchComponent:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Найти курс']")
    SUGGESTIONS_LIST = (By.CSS_SELECTOR, "div[data-testid='search-suggestions'] div")

    def __init__(self, driver):
        self.driver = driver

    def search_course(self, query):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)

    def get_suggestions(self):
        return [el.text for el in self.driver.find_elements(*self.SUGGESTIONS_LIST)]

    def select_suggestion(self, index=0):
        suggestions = self.driver.find_elements(*self.SUGGESTIONS_LIST)
        if suggestions:
            suggestions[index].click()

    def is_search_param_in_url(self, search_text):
        current_url = self.driver.current_url
        decoded_url = unquote(current_url)
        return f"search={search_text}" in decoded_url