import pytest
from po.landing_page import LandingPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


#  poetry run pytest --html=reports/report.html tests/.
class TestLandingPage:

    def test_landing_page_google(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_landing_page()

        try:
            google_header = landing_page.find(
                (By.XPATH, "//a[contains(text(), 'Google')]")
            )
            assert google_header.is_displayed(), "Google element displayed."
        except NoSuchElementException:
            landing_page.save_screenshot(self.test_landing_page_amazon.__name__)
            raise AssertionError("Google header does not exist.")

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
