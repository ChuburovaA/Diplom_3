import allure

from locators.recover_password_locators import RecoverPasswordLocators
from pages.base_page import BasePage


class RecoverPage(BasePage):
    @allure.step('Ввод email в поле для восстановления пароля')
    def set_email_for_recover_password(self, email):
        self.set_text_to_element(RecoverPasswordLocators.INPUT_EMAIL, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recover_button(self):
        self.move_to_element_and_click(RecoverPasswordLocators.RECOVER_BUTTON)

    @allure.step('Клик по иконке Показать/скрыть пароль')
    def click_on_show_password_icon(self):
        self.click_to_visible_element(RecoverPasswordLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка отображения кнопки "Сохранить"')
    def find_element_save_button(self):
        return self.find_element(RecoverPasswordLocators.SAVE_BUTTON)

    @allure.step('Проверка активности поля "Пароль"')
    def find_element_input_password_active(self):
        return self.find_element(RecoverPasswordLocators.INPUT_PASSWORD_ACTIVE)
