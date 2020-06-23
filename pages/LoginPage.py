import allure


class LoginPage:

    def __init__(self, driver):
        self._driver = driver
        self._input_field = "//input[@id='text']"
        self._search_button = "//button"

    @allure.step("Поиск")
    def search(self, filter):
        self._driver.find_element_by_xpath(self._input_field).send_keys(filter)
        self._driver.find_element_by_xpath(self._search_button).click()