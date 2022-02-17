import random
from Page_Object.AdminPage import AdminPage
import allure


@allure.title("Тест добавления товара через админку")
def test_add_new_product(browser, url):
    admin_page = AdminPage(browser, url)
    admin_page.open()
    admin_page.autorization_admin_page(login='user', password='bitnami')
    admin_page.open_products_list()
    name_product = f'Tesla m_ + {random.randint(1, 999)}'
    admin_page.add_new_product(product_name=name_product)


@allure.title("Тест удаления товра через админку")
def test_delete_product(browser, url):
    admin_page = AdminPage(browser, url)
    admin_page.open()
    admin_page.autorization_admin_page(login='user', password='bitnami')
    admin_page.open_products_list()
    admin_page.delete_product()
