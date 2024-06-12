from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage

import time

class LoginPage(BasePage):

    INPUT_E_MAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    SUMBIT = (By.CSS_SELECTOR, "[type='submit']")
    LOGO = (By.CSS_SELECTOR, "#logo > a")

    # авторизация в системе

    def login(self, e_mail, password):
        self._input(self.element(self.INPUT_E_MAIL), e_mail)
        self._input(self.element(self.INPUT_PASSWORD), password)

        self.logger.info("Click 'CONTINUE'")
        self.click(self.element(self.SUMBIT))

        time.sleep(2)
        self.logger.info("Go to MainPage")
        self.click(self.element(self.LOGO))