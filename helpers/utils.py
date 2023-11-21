import time

from selenium.webdriver.common.by import By


class Utils:

    def find_element_xpath(self, driver, element):
        return driver.find_element(By.XPATH, element)

