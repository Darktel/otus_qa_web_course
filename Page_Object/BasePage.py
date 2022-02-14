from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, self.browser.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        self.logger.info("search element: {}".format(locator))
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        self.logger.info("Clicking element: {}".format(element))
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        element.click()

    def _click_alert(self):
        try:
            self.browser.switch_to.alert.accept()
            self.logger.info("click to alert")
        except:
            pass

    def _click(self, locator: tuple):
        self.logger.info("Clicking element: {}".format(locator))
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)
