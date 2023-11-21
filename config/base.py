from selenium import webdriver


class Base:
    # Set a custom User-Agent for Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "user-agent=Chrome/91.0.4472.124")

    # Create a WebDriver instance with the custom User-Agent
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)

    def open_url(self):
        self.setup_method()
        self.driver.quit()

    def setup_method(self):
        self.driver.get("https://aloware.com/")
        print("driver session id from setup:", self.driver.session_id)

    def quit_driver(self):
        self.driver.quit()
