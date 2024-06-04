import allure
from conftests import *

from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.account_page import AccountPage

@allure.story('Тесты на проверку созданных заказов')
class TestOrderPage:

    @allure.title('Всплывающее окно с деталями заказа')
    def test_order_detalis_popup(self, driver):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)

        header_page.click_orders_list_button()
        order_page.click_order()

        assert order_page.check_element_order_structure().is_displayed()

    @allure.title('Проверка отображения созданного заказа в "Ленте заказов"')
    def test_new_order_in_order_list(self, driver, login_user):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)
        order_page = OrderPage(driver)

        main_page.make_order_and_get_order_number()
        header_page.click_user_account_button()
        account_page.click_account_button()

        account_page.click_on_order_list()
        account_page.find_element_order_status()
        order_number = account_page.get_order_number()

        header_page.click_orders_list_button()
        order_page.visibility_element_list_title()

        order = order_page.get_order_in_orderlist(order_number)

        assert order.is_displayed()

    @allure.title('Проверка изменения счетчика "Выполнено за все время" после создания нового заказа')
    def test_counter_total_orders_after_a_new_order(self, driver, login_user):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)

        main_page.find_element_ingredient_bun()
        header_page.click_orders_list_button()

        order_page.visibility_element_list_title()
        number_total_order = order_page.get_total_orders_number()

        header_page.click_constructor_button()
        main_page.wait_visibility_element_burger_constructor_title()

        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_button()
        order_page.visibility_element_list_title()
        new_number_total_order = order_page.get_total_orders_number()

        assert int(new_number_total_order) == int(number_total_order) + 1

    @allure.title('Проверка изменения счетчика "Выполнено за сегодня" после создания нового заказа')
    def test_counter_today_order_after_a_new_order(self, driver, login_user):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)

        main_page.find_element_ingredient_bun()
        header_page.click_orders_list_button()

        order_page.visibility_element_list_title()
        number_today_order = order_page.get_today_orders_number()

        header_page.click_constructor_button()
        main_page.wait_visibility_element_burger_constructor_title()
        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_button()
        order_page.visibility_element_list_title()
        new_number_today_order = order_page.get_today_orders_number()

        assert int(new_number_today_order) == int(number_today_order) + 1

    @allure.title('Проверка отображения нового заказа в списке "В работе"')
    def test_new_order_appears_in_work_list(self, driver, login_user):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)

        new_order = main_page.make_order_and_get_order_number()
        header_page.click_orders_list_button()
        order_page.wait_visibility_element_all_orders_ready_text()
        order_page.wait_visibility_element_order_in_work_number()
        order_in_work = order_page.get_order_number_in_work()

        assert new_order in order_in_work