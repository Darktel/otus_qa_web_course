from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegisterPage:
    path = "index.php?route=account/register"

    "/index.php?route=account/register"

    (By.CSS_SELECTOR, '#input-firstname')

    (By.CSS_SELECTOR, '#input-lastname')
    (By.CSS_SELECTOR, '#input-email')
    (By.CSS_SELECTOR, '#input-telephone')
    (By.CSS_SELECTOR, '#input-password')
    (By.CSS_SELECTOR, '#input-confirm')
    (By.CSS_SELECTOR, '')

    TITLE_PAGE = (By.CSS_SELECTOR, "#content > h1")
    check_box = (By.CSS_SELECTOR, "input[type=checkbox]:nth-child(2)")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url + self.path

    def open(self):
        self.browser.get(self.url)
        return self


