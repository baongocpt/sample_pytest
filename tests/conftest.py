import pytest
from core.web.base.DriverFactory import WebDriverFactory


@pytest.fixture()
def setUp():
    print("\nRunning method level setUp")
    yield
    print("\nRunning method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetup(request):
    print("\nRunning one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_browser_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\nRunning one time tearDown")


# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
