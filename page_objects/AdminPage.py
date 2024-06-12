from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
import time

class AdminPage(BasePage):

    LOGIN_FORM_LOGIN = (By.CSS_SELECTOR, "#input-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, ".btn")

    def login(self, login, password):
        self.logger.info("Enter administrator details")
        self.logger.info("Enter administrator login")
        self._input(self.element(self.LOGIN_FORM_LOGIN), login)
        self.logger.info("Enter administrator password")
        self._input(self.element(self.LOGIN_FORM_PASSWORD), password)
        
        self.logger.info("Click on 'Login'")
        self.click(self.element(self.LOGIN_FORM_BUTTON))


    NAV_CATALOG = (By.CSS_SELECTOR, "#menu-catalog > a:nth-child(1)")
    NAV_CATALOG_CATEGORIES = (By.CSS_SELECTOR, "#collapse-1 > li:nth-child(1) > a:nth-child(1)")
    ADD_NEW = (By.CSS_SELECTOR, "a.btn:nth-child(2)")
    ADD_GENERAL_NAME = (By.CSS_SELECTOR, "#input-name-1")
    ADD_GENERAL_META_TAG = (By.CSS_SELECTOR, "#input-meta-title-1")
    ADD_CATEGORY_SEO = (By.CSS_SELECTOR, "#form-category > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    ADD_SEO_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")
    ADD_SAVE = (By.CSS_SELECTOR, "div.float-end > button:nth-child(1)")

    LOGO = (By.CSS_SELECTOR, ".navbar-brand")
    
    def open_catalog(self):
        self.logger.info("Click on 'Catalog'")
        self.click(self.element(self.NAV_CATALOG))

    def add_category(self, category_name):
        self.logger.info("Click on 'Categories'")
        self.click(self.element(self.NAV_CATALOG_CATEGORIES))
        self.logger.info("Click on 'Add new'")
        self.click(self.element(self.ADD_NEW))

        self.logger.info("Enter category name")
        self._input(self.element(self.ADD_GENERAL_NAME), category_name)
        self.logger.info("Enter category meta tag title")
        self._input(self.element(self.ADD_GENERAL_META_TAG), category_name)

        self.logger.info("Click on 'SEO'")
        self.click(self.element(self.ADD_CATEGORY_SEO))
        self.logger.info("Enter keyword")
        self._input(self.element(self.ADD_SEO_KEYWORD), category_name.replace(' ', '-'))

        self.logger.info("Click on 'Save'")
        self.click(self.element(self.ADD_SAVE))

        self.logger.info("Click on 'Logo'")
        self.click(self.element(self.LOGO))


    """ = (By.CSS_SELECTOR, "") """
    NAV_CATALOG_PRODUCTS = (By.CSS_SELECTOR, "#collapse-1 > li:nth-child(2) > a:nth-child(1)")
    ADD_GENERAL_DESCRIPTION = (By.CSS_SELECTOR, ".cke_wysiwyg_frame")
    IFRAME_DESCRIPTION_P = (By.CSS_SELECTOR, "body > p:nth-child(1)")
    ADD_PRODUCT_DATA = (By.CSS_SELECTOR, "#form-product > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    ADD_PRODUCT_DATA_MODEL = (By.CSS_SELECTOR, "#input-model")
    ADD_PRODUCT_LINKS = (By.CSS_SELECTOR, "#form-product > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    ADD_PRODUCT_LINKS_CATEGORIES = (By.CSS_SELECTOR, "#input-category")
    ADD_PRODUCT_SEO = (By.CSS_SELECTOR, "li.nav-item:nth-child(11) > a:nth-child(1)")

    def add_product(self, device_name, device_description, category_name):
        self.logger.info("Click on 'Products'")
        self.click(self.element(self.NAV_CATALOG_PRODUCTS))
        self.logger.info("Click on 'Add new'")
        self.click(self.element(self.ADD_NEW))

        self.logger.info("Enter product name")
        self._input(self.element(self.ADD_GENERAL_NAME), device_name)

        self.logger.info("Enter product description")
        self._input_in_frame(self.element(self.ADD_GENERAL_DESCRIPTION), device_description)

        self.logger.info("Enter product meta tag title")
        self._input(self.element(self.ADD_GENERAL_META_TAG), device_name)

        self.logger.info("Click on 'Data'")
        self.click(self.element(self.ADD_PRODUCT_DATA))
        self.logger.info("Enter product model")
        self._input(self.element(self.ADD_PRODUCT_DATA_MODEL), device_name)

        self.logger.info("Click on 'Links'")
        self.click(self.element(self.ADD_PRODUCT_LINKS))
        self.logger.info("Enter product category")
        self._input(self.element(self.ADD_PRODUCT_LINKS_CATEGORIES), category_name)

        self.logger.info("Click on 'SEO'")
        self.click(self.element(self.ADD_PRODUCT_SEO))
        self.logger.info("Enter keyword")
        self._input(self.element(self.ADD_SEO_KEYWORD), device_name.replace(' ', '-'))

        self.logger.info("Click on 'Save'")
        self.click(self.element(self.ADD_SAVE))

        self.logger.info("Click on 'Logo'")
        self.click(self.element(self.LOGO))
    

    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".fa-trash-can")

    def delete_product(self, product):
        self.logger.info("Click on 'Products'")
        self.click(self.element(self.NAV_CATALOG_PRODUCTS))

        time.sleep(1)

        self.logger.info("Input product name in filter")
        self._input(self.element(self.FILTER_PRODUCT_NAME), product)

        self.logger.info("Click on 'Filter'")
        self.click(self.element(self.FILTER_BUTTON))

        time.sleep(1)

        self.logger.info("Click on product checkbox")
        self.click(self.element(self.PRODUCT_CHECKBOX))

        self.logger.info("Click on 'Delete'")
        self.click(self.element(self.DELETE_BUTTON))

        self.logger.info("Click on 'OK' in alert")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
