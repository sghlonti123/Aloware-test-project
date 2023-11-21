import time

from page.mainPage import MainPage

mainPage = MainPage()


class TestDemo:

    def test_ATP_1(self):
        assert mainPage.get_page_title() == "Top-Rated Contact Center Software | Built For Your Favorite CRM"
