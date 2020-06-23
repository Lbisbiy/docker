import allure
import pytest

from data.TestData import TestData
from pages.LoginPage import LoginPage


class TestLogin:
    def test_authenticate(self, driver):
        driver.get(TestData.BASE_URL)
        page = LoginPage(driver)
        page.search('google')