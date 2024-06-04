import allure

from conftests import *
from pages.main_page import MainPage

@allure.story('Тесты на стартовой странице Stellar Burgers')
class TestMainPage:

    @allure.title('Появление всплывающего окна при нажатии на ингредиент')
    def test_open_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun()

        popup_text = main_page.check_counter_of_detail_popup()

        assert popup_text == 'Детали ингредиента'

    @allure.title('Закрытие высплывающего окна с инфомацией об ингредиенте при нажатии на "крестик"')
    def test_close_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_bun()
        main_page.click_close_button()
        main_page.check_text_of_ingredients_counter()

        assert not main_page.check_text_of_ingredients_counter().is_displayed()

    @allure.title('Изменение счетчика ингредиента')
    def test_change_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        start_quantity = main_page.check_counter_of_ingredients()
        main_page.add_filling_to_order_basket()
        end_quantity = main_page.check_counter_of_ingredients()

        assert end_quantity > start_quantity

    @allure.title('Создание заказа')
    def test_make_order(self, driver, login_user):
        main_page = MainPage(driver)

        main_page.find_element_ingredient_bun()
        main_page.add_bun_to_order_basket()
        main_page.add_sauce_to_order_basket()
        main_page.click_order_button()
        main_page.find_element_order_number_text()

        assert main_page.check_element_order_status().is_displayed() == True
