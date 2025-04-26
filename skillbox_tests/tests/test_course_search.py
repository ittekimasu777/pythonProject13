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


def test_search_relevant_suggestions(landing_page):

    landing_page.open_all_courses()

    test_cases = [
        ("тестиров", ["Тестирование", "Тестировщик"]),
        ("python", ["Python"]),
        ("дизайн", ["Дизайн", "Графический дизайн"])
    ]

    for query, expected_keywords in test_cases:
        landing_page.search.search_course(query)
        suggestions = landing_page.search.get_suggestions()

        assert suggestions, f"No suggestions for query: {query}"

        for keyword in expected_keywords:
            assert any(keyword.lower() in s.lower() for s in suggestions), \
                f"Keyword '{keyword}' not found in suggestions for query '{query}'"


def test_search_case_insensitive(landing_page):

    landing_page.open_all_courses()

    test_cases = [
        ("PYTHON", ["Python"]),
        ("ТеСтИрОвЩиК", ["Тестировщик"])
    ]

    for query, expected_keywords in test_cases:
        landing_page.search.search_course(query)
        suggestions = landing_page.search.get_suggestions()

        assert suggestions, f"No suggestions for query: {query}"

        for keyword in expected_keywords:
            assert any(keyword.lower() in s.lower() for s in suggestions), \
                f"Keyword '{keyword}' not found in suggestions for query '{query}'"


def test_navigation_by_suggestion(landing_page):

    landing_page.open_all_courses()

    test_queries = ["Python", "Тестировщик", "Маркетинг"]

    for query in test_queries:
        landing_page.search.search_course(query)
        landing_page.search.select_suggestion(0)

        assert landing_page.search.is_search_param_in_url(query), \
            f"Search parameter '{query}' not found in URL after navigation"

        landing_page.driver.back()
        landing_page.open_all_courses()