from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class SearchPage(BasePage):

    PRODUCT_LINK = (By.CSS_SELECTOR, ".description > h4:nth-child(1) > a:nth-child(1)")

    def click_on_product(self):
        self.logger.info("Click on a product")
        self.click(self.element(self.PRODUCT_LINK))
    
    RESULTS = (By.CSS_SELECTOR, "#product-list > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(1) > a:nth-child(1)")

    def get_results(self):
        self.logger.info("Get search result")
        return [elem.text for elem in self.elements(self.RESULTS)]