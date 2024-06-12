from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class WishlistPage(BasePage):

    WISHLIST = (By.CSS_SELECTOR, "#wishlist")
    PRODUCTS_NAME = (By.CSS_SELECTOR, "td.text-start > a")

    def get_products_names(self):
        products_name = []

        self.logger.info("Get products in Wishlist")
        wish_list = self.element(self.WISHLIST)

        for product in wish_list.find_elements(*self.PRODUCTS_NAME):
            products_name.append(product.text)
        
        return products_name
