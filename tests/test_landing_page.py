import pytest
from po import landing_page
from po.landing_page import LandingPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


#  poetry run pytest --html=reports/report.html tests/.
# HEADLESS=false poetry run pytest --html=reports/report.html tests/
# BROWSER=firefox HEADLESS=false poetry run pytest --html=reports/report.html tests/


class TestLandingPage:

    def test_landing_page_google_pass(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_url("https://www.google.com/")

        try:
            assert (
                landing_page.current_url == "https://www.google.com/"
            ), f"Expected URL to be 'https://www.google.com/', but got '{landing_page.current_url}'"
        except AssertionError as e:
            landing_page.save_screenshot(self.test_landing_page_google.__name__)
            raise e

    def test_landing_page_google_fail(self, driver):  # this will fail on purpose
        landing_page = LandingPage(driver)
        landing_page.open_url("https://www.amazon.com/")

        try:
            assert (
                landing_page.current_url == "https://www.google.com/"
            ), f"Expected URL to be 'https://www.google.com/', but got '{landing_page.current_url}'"
        except AssertionError as e:
            landing_page.save_screenshot(self.test_landing_page_google.__name__)
            raise e

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
