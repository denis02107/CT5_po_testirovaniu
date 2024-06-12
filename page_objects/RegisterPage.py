from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class RegisterPage(BasePage):

    # 4.	Пройти через меню в регистрацию, заполнить все поля и нажать «зарегистрироваться».

    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstname']")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input[name='lastname']")
    INPUT_E_MAIL = (By.CSS_SELECTOR, "input[name='email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_PRIVACY_POLICY = (By.CSS_SELECTOR, "input[name='agree']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "button[type='submit']")

    def register(self, firstname, lastname, e_mail, password):
        self._input(self.element(self.INPUT_FIRST_NAME), firstname)
        self._input(self.element(self.INPUT_LAST_NAME), lastname)
        self._input(self.element(self.INPUT_E_MAIL), e_mail)
        self._input(self.element(self.INPUT_PASSWORD), password)

        self.logger.info("Click 'AGREE'")
        self.click(self.element(self.BUTTON_PRIVACY_POLICY))
        self.logger.info("Click 'CONTINUE'")
        self.click(self.element(self.BUTTON_CONTINUE))