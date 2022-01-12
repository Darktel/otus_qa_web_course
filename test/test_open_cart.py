from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import random, time


def test_main_page(browser, url):
    '''
    Тесты на главную страницу url:https://demo.opencart.com/
    :param browser:
    :param url: 'https://demo.opencart.com/'
    '''
    browser.get(url)
    # Проверка, что колличество элементов в верхней части страницы не изменяется = 7
    header_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "top-links")))
    elements = header_links.find_elements(By.TAG_NAME, 'li')
    assert len(elements) == 7
    # Проверка что первый элемент в избранном действительно macBook. (сталкивался с таким биз. требованием в реальности)
    freature_product = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-layout")))
    assert 'MacBook' in freature_product.text
    # Поиск на странице кнопки Корзины.
    button_cart = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart [type='button']")))
    assert button_cart.tag_name == 'button'
    # Проверка футера страницы на наличие ссылки О Нас (About Us)
    footer_imformation = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "footer [class='list-unstyled'] [href]")))
    assert footer_imformation.text == 'About Us'
    # Проверка строки поиска - у элемента строки поиска тег input (поле для ввода данных)
    search = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#search [name='search']")))
    assert search.tag_name == 'input'


def test_catalog_page(browser, url):
    '''
    Тесты на каталог товаров - https://demo.opencart.com/index.php?route=product/category&path=20
    :param browser:
    '''
    browser.get(url + "index.php?route=product/category&path=20")

    section_title = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content h2")))
    assert section_title.text == 'Desktops'

    sort_by = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-sort option:first-child")))
    assert sort_by.get_property('selected')

    cart_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart")))
    assert cart_btn.is_enabled()

    show_by = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-limit option[selected='selected']")))
    assert int(show_by.text) == 15  # кол-во элементов на странице поумолчению.

    # Колличество товаров на странице ограничивается выбранным значением в фильтре.
    products = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content div:nth-child(7):not(.product-layout)")))
    assert len(products.find_elements(By.CSS_SELECTOR, "div.product-layout")) < int(show_by.text)


def test_product_card(browser, url):
    '''
    Карточку товара - https://demo.opencart.com/index.php?route=product/product&path=20&product_id=44
    :param browser:
    '''
    browser.get(url + "index.php?route=product/product&path=20&product_id=44")
    # Тест на корректное наименование товара
    assert WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#product-product > ul > li:last-child > a"))).text == 'MacBook Air'
    # Тест проверки цены товара
    price = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) h2"))).text
    assert price == '$1,202.00'
    # Тест на доступность кнопки "Add to Cart"
    assert WebDriverWait(browser, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#button-cart"))).get_property('type') == 'button'
    # тест на успешное добавление товара в сравнение.
    WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-original-title='Compare this Product']"))).click()
    assert WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#product-product > div.alert.alert-success.alert-dismissible"))).text == 'Success: You have added MacBook Air to your product comparison!\n×'

    # проверка верного кол-ва добавления товара в корзину.
    count_product = random.randint(1, 10)
    quantity = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-quantity")))
    quantity.click()
    quantity.clear()
    quantity.send_keys(f'{count_product}')
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#button-cart"))).click()
    time.sleep(1)
    assert f'{count_product} item(s)' in WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#cart-total"))).text


def test_login_admin_page(browser, url):
    '''
    Страницу логина в админку /admin
    :param browser:
    '''
    browser.get(url + "/admin/")
    input_login = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "input-username")))
    assert input_login.get_attribute("placeholder") == "Username"
    input_password = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "input-password")))
    assert input_password.get_attribute("placeholder") == "Password"

    button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    assert button.get_property('type') == 'submit'
    assert button.text == 'Login'

    input_login.clear()
    input_login.send_keys('demo')
    input_password.clear()
    input_password.send_keys('demo')
    button.click()
    assert WebDriverWait(browser, 4).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#header > div > ul > li.dropdown > a"))).text == "demo demo"


@pytest.mark.parametrize('localor', (
        '#input-firstname', '#input-lastname', '#input-email', '#input-telephone', '#input-password', '#input-confirm'))
def test_registration_page(browser, url, localor):
    '''
    Страницу регистрации пользователя (/index.php?route=account/register)
    :param browser:
    '''
    browser.get(url + "/index.php?route=account/register")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, localor))).is_displayed()


def test_registration_page_2(browser, url):
    '''
    Страницу регистрации пользователя (/index.php?route=account/register)
    :param browser:
    '''
    browser.get(url + "/index.php?route=account/register")
    assert WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h1"))).text == "Register Account"
    assert WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type=checkbox]:nth-child(2)"))).get_property(
        'type') == "checkbox"
