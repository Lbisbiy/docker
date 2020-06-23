import pytest

from helpers.DriverHelper import DriverHelper


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default=""
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(autouse=True)
def driver(request):
    web_driver = DriverHelper("").webdriver
    yield web_driver
    web_driver.close()
