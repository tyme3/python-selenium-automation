from Pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.driver.get('https://www.target.com/')
