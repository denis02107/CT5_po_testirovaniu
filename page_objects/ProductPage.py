from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage

from selenium.webdriver.support.ui import Select

import time

class ProductPage(BasePage):

    # 1.   Кликнуть на продукт на главной странице, проверить переключение скриншотов на странице с продуктом.

    SCREEN_SWITCH_OPEN = (By.CSS_SELECTOR, "img.mb-3")
    SCREEN_SWITCH_SCREEN_COUNTER = (By.CSS_SELECTOR, ".mfp-counter")
    SCREEN_SWITCH_ARROW_LEFT = (By.CSS_SELECTOR, "button.mfp-arrow-left")
    SCREEN_SWITCH_ARROW_RIGHT = (By.CSS_SELECTOR, "button.mfp-arrow-right")
    SCREEN_SWITCH_CLOSE = (By.CSS_SELECTOR, "button.mfp-close")

    def open_screens(self):
        self.logger.info("Open screens")
        self.element(self.SCREEN_SWITCH_OPEN).click()

    def get_screens_counter(self):
        self.logger.info("Get screens counter")
        return int(self.element(self.SCREEN_SWITCH_SCREEN_COUNTER).text[-1])
    
    def click_screen_left_arrow(self):
        self.logger.info("Click on 'previous screen'")
        self.element(self.SCREEN_SWITCH_ARROW_LEFT).click()

    def click_screen_right_arrow(self):
        self.logger.info("Click on 'next screen'")
        self.element(self.SCREEN_SWITCH_ARROW_RIGHT).click()

    def close_screens(self):
        self.logger.info("Close screens")
        self.element(self.SCREEN_SWITCH_CLOSE).click()

    # 7. Добавление в корзину
    
    SELECT_COLOR = (By.CSS_SELECTOR, "#input-option-226")

    ADD_TO_CART = (By.CSS_SELECTOR, "#button-cart")

    def add_to_cart(self):
        color_selection = self.driver.find_elements(*self.SELECT_COLOR)

        if color_selection:
            self.logger.info("Chose product color")
            Select(color_selection[0]).select_by_index(1)
        
        self.logger.info("Click 'ADD TO CART'")
        self.click(self.element(self.ADD_TO_CART))
    
    CART_BUTTON = (By.CSS_SELECTOR, "button.btn-lg:nth-child(1)")
    VIEW_CART = (By.CSS_SELECTOR, "p.text-end > a:nth-child(1) > strong:nth-child(1)")

    def go_to_Cart_Page(self):
        self.logger.info("Open CartPage")
        self.click(self.element(self.CART_BUTTON))
        self.click(self.element(self.VIEW_CART))
    
    # 10. Написание отзыва
    
    WRITE_REVIEW = (By.CSS_SELECTOR, ".rating > p:nth-child(1) > a:nth-child(7)")
    TEXT_REVIEW = (By.CSS_SELECTOR, "#input-text")
    RATING = (By.CSS_SELECTOR, "input[name='rating']")
    REVIEW_BUTTON = (By.CSS_SELECTOR, "#button-review")

    def write_review(self, review_text, product_rating):
        self.logger.info("Click 'Write a review'")
        self.click(self.element(self.WRITE_REVIEW))

        self.logger.info("Input review text")
        self._input(self.element(self.TEXT_REVIEW), review_text)

        self.scroll_to_the_bottom_page()
        time.sleep(2)

        self.logger.info("Choose product rating")
        self.click(self.elements(self.RATING)[product_rating])

        self.logger.info("Click 'Send Review'")
        self.click(self.element(self.REVIEW_BUTTON))



