import allure

from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_to_visible_element(HeaderPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_orders_list_button(self):
        self.move_to_element_and_click(HeaderPageLocators.ORDERS_LIST_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_user_account_button(self):
        self.move_to_element_and_click(HeaderPageLocators.ACCOUNT_BUTTON)