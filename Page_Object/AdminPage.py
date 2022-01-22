from selenium.webdriver.common.by import By

from .BasePage import BasePage


path = "/admin/"

input_login = (By.ID, "input-username")

input_password = (By.ID, "input-password")


button_submit = (By.CSS_SELECTOR, "button[type='submit']")

"demo demo" = (By.CSS_SELECTOR, "#header > div > ul > li.dropdown > a")