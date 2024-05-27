from Pages.main_page import MainPage
from Pages.header import Header
from Pages.search_results import SearchResultsPage
from Pages.base_page import Page



class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultsPage(driver)


