from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CartPage(BasePage):

    PRODUCT_NAME = (By.CSS_SELECTOR, ".text-wrap > a:nth-child(1)")

    def get_product_name(self):
        self.logger.info("Get product name")
        return self.element(self.PRODUCT_NAME).text