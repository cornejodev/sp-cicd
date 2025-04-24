from selenium.webdriver.remote.webdriver import WebDriver
from po.base_page import BasePage


class LandingPage(BasePage):
    url = "https://www.amazon.com.mx/"
    url_2 = "https://www.google.com/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_landing_page(self):
        super().open_url(self.url_2)

    def open_landing_page_produce_error(self):
        super().open_url(self.url)
