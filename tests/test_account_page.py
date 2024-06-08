import pytest
import allure

from data import Urls
from conftests import *

from pages.account_page import AccountPage
from pages.header_page import HeaderPage

@allure.story('Тесты на проверку "Личный кабинет"')
class TestAccountPage:

    @allure.title('Проверяем клик на "Личный кабинет" в шапке')
    def test_click_to_account_from_header(self, driver, login_user):
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)

        header_page.click_user_account_button()
        account_page.click_account_button()

        assert account_page.get_current_url() == Urls.profile_user_page

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_click_to_order_history(self, driver, login_user):
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)

        header_page.click_user_account_button()
        account_page.click_account_button()
        account_page.click_on_order_list()

        assert account_page.get_current_url() == Urls.orders_history

    @allure.title('Проверка выхода из аккаунта')
    def test_log_out_account(self, driver,login_user):
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)

        header_page.click_user_account_button()
        account_page.click_account_button()
        account_page.click_logout_button()
        account_page.click_to_enter_button()

        text_in_button = account_page.get_text_of_enter_button()

        assert text_in_button == 'Войти'