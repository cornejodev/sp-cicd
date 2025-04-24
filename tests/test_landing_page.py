import pytest
from po import landing_page
from po.landing_page import LandingPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


#  poetry run pytest --html=reports/report.html tests/.
class TestLandingPage:

    def test_landing_page_google(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_landing_page()

        locator = (By.XPATH, "//a[contains(text(), 'Google')]")

        try:
            landing_page.wait_until_element_is_visible(locator)
            assert landing_page.is_displayed(locator), "Google link should be visible"
        except TimeoutException or NoSuchElementException:
            landing_page.save_screenshot(self.test_landing_page_google.__name__)
            raise AssertionError("Google link not visible in time")

    # def test_landing_page_amazon(self, driver):  # will fail on purpose
    #     landing_page = LandingPage(driver)
    #     landing_page.open_landing_page_produce_error()

    #     try:
    #         google_header = landing_page.find(
    #             (By.XPATH, "//a[contains(text(), 'Google')]")
    #         )
    #         assert google_header.is_displayed(), "Google element displayed."
    #     except NoSuchElementException:
    #         landing_page.save_screenshot(self.test_landing_page_amazon.__name__)
    #         raise AssertionError("Google header does not exist.")
