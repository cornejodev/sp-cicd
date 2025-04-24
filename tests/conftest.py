import os
import base64
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# HEADLESS=false poetry run pytest --html=reports/report.html tests/
# BROWSER=firefox HEADLESS=false poetry run pytest --html=reports/report.html tests/


@pytest.fixture(scope="function")
def driver():
    browser = os.getenv("BROWSER", "chrome")
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    print(f"Launching {browser} (headless={headless})")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--user-data-dir=/tmp/chrome-profile")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser to execute tests (chrome or firefox)",
    )


def pytest_html_report_title(report):
    report.title = "Amazon Test Suite Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])
    if report.when == "call":
        # Get the project's root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Construct the relative path to the screenshot based on the test method name
        screenshot_filename = f"{item.name}.png"
        screenshot_path = os.path.join(
            project_root, "reports", "screenshots", screenshot_filename
        )

        if os.path.exists(screenshot_path):
            with open(screenshot_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            extra.append(pytest_html.extras.png(encoded_string))

        report.extras = extra


# $x('//nav/ol/li/a[contains(text(),"Women")]/text()').map(x=>x.wholeText)
