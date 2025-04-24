import os
import base64
import pytest
import pytest_html

from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise ValueError(f"Expected 'chrome' or 'firefox', but got {browser}")
    my_driver.maximize_window()
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


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

