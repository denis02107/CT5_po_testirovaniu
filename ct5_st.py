from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.CategoryPage import CategoryPage
from page_objects.RegisterPage import RegisterPage
from page_objects.LoginPage import LoginPage
from page_objects.WishlistPage import WishlistPage
from page_objects.CartPage import CartPage
from page_objects.SearchPage import SearchPage
from page_objects.AdminPage import AdminPage
import time

import allure

# 1.   Кликнуть на продукт на главной странице, проверить переключение скриншотов на странице с продуктом.
@allure.feature("Product")
@allure.title("Check the screenshot switching")
def test_product_screens(driver):
    MainPage(driver).click_featured_product(3)
    
    ProductPage(driver).open_screens()

    screens_number = ProductPage(driver).get_screens_counter()

    for _ in range(screens_number):
        ProductPage(driver).click_screen_right_arrow()
        driver.implicitly_wait(1)
    
    for _ in range(screens_number):
        ProductPage(driver).click_screen_left_arrow()
        driver.implicitly_wait(1)

    ProductPage(driver).close_screens()


# 2.	Сменить валюту на главной странице с доллара на евро и обратно.
@allure.feature("Menu")
@allure.story("Click on menu")
@allure.title("Change currency")
def test_change_currency(driver):
    
    currency_before_change = MainPage(driver).get_current_currency()
    MainPage(driver).change_the_currency(0)
    currency_changed = MainPage(driver).get_current_currency()
    MainPage(driver).change_the_currency(2)
    current_currency = MainPage(driver).get_current_currency()

    assert currency_before_change == current_currency, "Изначальная и текущая валюта отличаются"
    assert currency_before_change == "$", "Изначальная и текущая валюта не были долларом"
    assert currency_changed == "€", "Валюта сменилась не на евро"


# 3.	Перейти через меню в категорию PC, проверить, что страница пуста.
@allure.feature("Product category")
@allure.story("PC caregory is empty")
@allure.title("Check PC category")
def test_PC_category_empty(driver):
    MainPage(driver).open_menu(0)
    MainPage(driver).go_to_category_in_menu(0)
    
    empty_content = CategoryPage(driver).get_empty_content()

    assert empty_content == "There are no products to list in this category."


# 4.	Пройти через меню в регистрацию, заполнить все поля и нажать «зарегистрироваться».
@allure.feature("Register")
@allure.title("Check registration")
def test_register_user(driver):
    MainPage(driver).go_to_register_page()

    RegisterPage(driver).register("user", "test", "testuser@test.com", "12345")


# 5.	Написать в строке поиска на главной странице поисковое слово и нажать кнопку поиска (может выдать ошибку).
@allure.feature("Search")
@allure.title("Check search")
def test_search(driver):
    MainPage(driver).search('Canon')
    time.sleep(1)


# 6.    Добавление товара в вишлист
@allure.feature("Wishlist")
@allure.story("Add product to cart")
@allure.title("Add single product to wishlist")
def test_add_product_to_wishlist(driver):

    # авторизация
    MainPage(driver).go_to_Login_Page()
    LoginPage(driver).login("testuser@test.com", "12345")

    product_name = MainPage(driver).get_featured_product_name(0)

    MainPage(driver).add_featured_product_to_wishlist(0)
    time.sleep(8)

    MainPage(driver).go_to_Wishlist_Page()
    time.sleep(5)
    products_in_wishlist = WishlistPage(driver).get_products_names()

    assert product_name in products_in_wishlist

# 7.    Добавление камеры в корзину
@allure.feature("Shopping Cart")
@allure.story("Add product to cart")
@allure.title("Adding single product to cart")
def test_add_camera_to_cart(driver):
    product_name_to_cart = MainPage(driver).get_featured_product_name(3)
    MainPage(driver).click_featured_product(3)
    ProductPage(driver).add_to_cart()

    time.sleep(8)
    ProductPage(driver).go_to_Cart_Page()

    product_in_cart = CartPage(driver).get_product_name()

    assert product_name_to_cart == product_in_cart

# 8.    Добавление планшета в корзину
@allure.feature("Shopping Cart")
@allure.story("Add product to cart")
@allure.title("Adding single product to cart")
def test_add_table_to_cart(driver):
    MainPage(driver).search("Tab")
    time.sleep(3)
    
    SearchPage(driver).click_on_product()

    ProductPage(driver).add_to_cart()
    time.sleep(8)

    ProductPage(driver).go_to_Cart_Page()

    product_in_cart = CartPage(driver).get_product_name()

    assert "Tab" in product_in_cart

# 9.    Добавление телефона htc в корзину
@allure.feature("Shopping Cart")
@allure.story("Add product to cart")
@allure.title("Adding single product to cart")
def test_add_tel_htc_to_cart(driver):
    MainPage(driver).search("HTC")
    time.sleep(3)
    
    SearchPage(driver).click_on_product()

    ProductPage(driver).add_to_cart()
    time.sleep(8)

    ProductPage(driver).go_to_Cart_Page()

    product_in_cart = CartPage(driver).get_product_name()

    assert "HTC" in product_in_cart

# 10.   Написать отзыв (write review) на любой выбранный товар
@allure.feature("Product Page")
@allure.title("Check writting a review")
def test_write_review(driver):

    # авторизация
    MainPage(driver).go_to_Login_Page()
    LoginPage(driver).login("testuser@test.com", "12345")

    MainPage(driver).click_featured_product(3)

    ProductPage(driver).write_review("Good product!", 4)

    time.sleep(2)


# 11.   Создать через тесты в админ панели новую категорию «Devices»
"""
AdminPage:
1. Перейти по ссылке "localhost/administration/"

login(login, password):
2. Ввести данные админа: "user" - логин, "bitnami" - пароль
3. Нажать кнопку "Login"

add_category(category_name):
4. Нажать на "Catalog" в левом меню
5. Нажать на "Categories"
6. Нажать на "Add new"
7. В поле "Category Name" ввести "Devices"
8. В поле "Meta Tag Title" ввести "Devices"
9. Нажать на "SEO"
10. В поле "Keyword" ввести "Devices"
11. Нажать на "Save"
"""
def test_admin_add_new_category(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")

    AdminPage(driver).open_catalog()
    AdminPage(driver).add_category("Devices")
    time.sleep(5)

# 12.   Добавить через тесты 2 компьютерные мыши и 2 клавиатуры в категорию «Devices» с описанием
"""
AdminPage:
1. Перейти по ссылке "localhost/administration/"

login(login, password):
2. Ввести данные админа: "user" - логин, "bitnami" - пароль
3. Нажать кнопку "Login"

add_device(device_name, device_description, category_name):
4. Нажать на "Catalog" в левом меню
5. Нажать на "Products"
6. Нажать на "Add new"
7. В поле "Product Name" ввести device_name
8. В поле "Description" ввести device_description
9. В поле "Meta Tag Title" ввести device_name
10. Нажать на "Links"
11. В поле "Categories" ввести category_name
12. Нажать на "SEO"
13. В поле "Keyword" ввести device_name c заменой пробелов на "-"
14. Нажать на "Save"
"""

def test_admin_add_new_products(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    AdminPage(driver).open_catalog()

    products = [
        ['Keyboard GSX 1', 'The best keyboard for gamers', 'Devices'],
        ['Keyboard GSX PRO 3000', 'The best of the best keyboard for gamers', 'Devices'],
        ['Mouse GSM 13', 'Good model for beginners', 'Devices'],
        ['Mouse GSM 100', 'The best mouse for gamers', 'Devices']
        ]

    for product in products:
        name, description, category = product
        AdminPage(driver).add_product(name, description, category)
        time.sleep(1)
    
    time.sleep(3)

# 13.   После добавления, проверить через тестирование, что на главной странице через поиск отображаются созданные товары
"""
MainPage:
search():
1. Произвести поиск

SearchPage:
get_results():
2. Узнать результаты поиска

3. Проверить, что среди результатов есть искомый товар
"""

def test_show_added_products(driver):
    products = [ 'Keyboard GSX 1',
                 'Keyboard GSX PRO 3000',
                 'Mouse GSM 13',
                 'Mouse GSM 100' ]
    
    for product in products:
        MainPage(driver).search(product)
        time.sleep(1)
        assert product in SearchPage(driver).get_results()

# 14.   Удалить 1 мышь и 1 клавиатуру через админ-панель
"""
AdminPage:
1. Перейти по ссылке "localhost/administration/"

login(login, password):
2. Ввести данные админа: "user" - логин, "bitnami" - пароль
3. Нажать кнопку "Login"

open_catalog():
4. Нажать на "Catalog" в левом меню

delete_product(self, product):
5. Нажать на "Products"
6. Ввести product в фильтр Product Name
7. Нажать на "Filter"
8. Поставить галочку в строке товара
9. Нажать кнопку Удалить
10. Нажать кнопку ОК в появивщемся окне
"""

def test_admin_delete_products(driver):
    products_to_delete = ['Keyboard GSX PRO 3000',
                         'Mouse GSM 13']
    
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    AdminPage(driver).open_catalog()

    for product in products_to_delete:
        AdminPage(driver).delete_product(product)


# 15.   Проверить, что на главной странице отображаются только оставшиеся товары
def test_deleted_products(driver):
    deleted_products = ['Keyboard GSX PRO 3000',
                         'Mouse GSM 13']
    existing_products = ['Keyboard GSX 1',
                         'Mouse GSM 100']
    
    for product in deleted_products:
        MainPage(driver).search(product)
        time.sleep(1)
        assert product not in SearchPage(driver).get_results()

    for product in existing_products:
        MainPage(driver).search(product)
        time.sleep(1)
        assert product in SearchPage(driver).get_results()