import time

from config.base import Base
from helpers.utils import Utils

utils = Utils()


class MainPage(Base):

    def get_page_title(self):
        title = self.driver.title
        return title

    def get_page_url(self):
        url = self.driver.current_url
        return url

    def get_login_button(self):
        login_button = utils.find_element_xpath(self.driver, "//a[@class='login-btn hyper-hover-green']")
        return login_button
