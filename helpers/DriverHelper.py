from selenium import webdriver

CAPABILITIES = {
    "browserName": "chrome",
    "enableVnc": True
}


class DriverHelper:
    def __init__(self, url):
        self._driver = None
        self._url = url

    @property
    def webdriver(self):
        if not self._driver:
            if self._url == "":
                self._driver = webdriver.Chrome("../chromedriver")
            else:
                self._driver = webdriver.Remote(
                    command_executor=self._url,
                    desired_capabilities=CAPABILITIES
                )
        return self._driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._driver.close()

    def close(self):
        self._driver.close()