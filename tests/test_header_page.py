import allure

from data import Urls
from conftests import *

from pages.header_page import HeaderPage
from pages.order_page import OrderPage

@allure.story('Тесты на стартовой странице "Stellar Burgers"')
class TestHeaderPage:

    @allure.title('Переход в раздел "Конструктор"')
    def test_click_to_constructor_in_start_page(self, driver):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)

        header_page.click_orders_list_button()
        order_page.visibility_element_list_title()
        header_page.click_constructor_button()

        url = header_page.get_current_url()

        assert url == Urls.BASE_PAGE

    @allure.title('Переход в раздел "Лента заказов"')
    def test_click_to_order_list_in_start_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()

        url = header_page.get_current_url()

        assert url == Urls.order_feed