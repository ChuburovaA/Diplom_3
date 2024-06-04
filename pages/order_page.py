import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Получение заказа по номеру в Ленте заказов')
    def get_order_in_orderlist(self, order):
        method, locator = OrderPageLocators.ORDER_NUMBER
        locator = locator.format(order)
        return self.find_element((method, locator))

    @allure.step('Клик по заказу в списке Лента заказов')
    def click_order(self):
        self.click_to_visible_element(OrderPageLocators.ORDER_LINK)

    @allure.step('Получение заказа по номеру в разделе "В работе"')
    def get_order_number_in_work(self):
        return self.get_text_of_element(OrderPageLocators.ORDER_IN_WORK_NUMBER)

    @allure.step('Получение количества заказов выполненных за сегодня')
    def get_today_orders_number(self):
        return self.get_text_of_element(OrderPageLocators.COMPLETED_ORDERS_TODAY)

    @allure.step('Получение количества заказов выполненных за все время')
    def get_total_orders_number(self):
        return self.get_text_of_element(OrderPageLocators.COMPLETED_ORDERS_TOTAL)

    @allure.step('Проверка отображения заголовка "Лента заказов"')
    def visibility_element_list_title(self):
        self.wait_visibility_element(OrderPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Проверка отображения заголовка "Состав"')
    def check_element_order_structure(self):
        return self.check_element(OrderPageLocators.ORDER_STRUCTURE_TITLE)

    @allure.step('Проверка отображения текста "Все текущие заказы готовы!"')
    def wait_visibility_element_all_orders_ready_text(self):
        self.wait_visibility_element(OrderPageLocators.ALL_ORDERS_READY_TEXT)

    @allure.step('Проверка отображения номера заказа в работе')
    def wait_visibility_element_order_in_work_number(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_IN_WORK_NUMBER)
