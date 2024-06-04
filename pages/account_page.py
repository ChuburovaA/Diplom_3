import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage

class AccountPage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_account_button(self):
        self.wait_visibility_element(AccountPageLocators.PROFILE_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_button(self):
        self.click_to_visible_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_order_list(self):
        self.click_to_visible_element(AccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Получение номера заказа в "История заказов"')
    def get_order_number(self):
        return self.get_text_of_element(AccountPageLocators.ORDER_NUMBER)

    @allure.step('Получение статуса заказа в истории')
    def find_element_order_status(self):
        self.find_element(AccountPageLocators.ORDER_STATUS)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_password_recover_button(self):
        self.click_to_visible_element(AccountPageLocators.RESET_PASSWORD_BUTTON)

    @allure.step('Ввести данные в поле "Email"')
    def input_text_email(self, create_and_delete_user):
        self.set_text_to_element(AccountPageLocators.INPUT_EMAIL, create_and_delete_user[0]['email'])

    @allure.step('Ввести данные в поле "Пароль"')
    def input_text_password(self, create_and_delete_user):
        self.set_text_to_element(AccountPageLocators.INPUT_PASSWORD, create_and_delete_user[0]['password'])

    @allure.step('Клик по кнопке "Войти"')
    def click_to_enter_button(self):
        self.click_to_visible_element(AccountPageLocators.ENTER_BUTTON)

    @allure.step('Получение текста кнопки "Войти"')
    def get_text_of_enter_button(self):
        return self.get_text_of_element(AccountPageLocators.ENTER_BUTTON)

