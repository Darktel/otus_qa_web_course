from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url + self.path