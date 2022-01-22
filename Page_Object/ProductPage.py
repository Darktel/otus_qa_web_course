from selenium.webdriver.common.by import By

from .BasePage import BasePage

path = "index.php?route=product/product&path=20&product_id=44"

NAME_PRODUCT = (By.CSS_SELECTOR, "#product-product > ul > li:last-child > a")
    # Тест проверки цены товара
    price = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) h2")
    # Тест на доступность кнопки "Add to Cart"
    button-cart = (By.CSS_SELECTOR, "#button-cart")
BUTTON_Compare = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")
    ALLERT_COMPARE = (By.CSS_SELECTOR, "#product-product > div.alert.alert-success.alert-dismissible")

input-quantity =  (By.CSS_SELECTOR, "#input-quantity")

        button-cart = (By.CSS_SELECTOR, "#button-cart")

cart-total =  (By.CSS_SELECTOR, "#cart-total")