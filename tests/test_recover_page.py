import allure

from conftests import *
from data import Urls

from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from pages.recover_page import RecoverPage

@allure.story('Тесты на восстановление пароля')
class TestRecoverPasswordPage:

    @allure.title('Проверка перехода на страницу логина при клике на "Восстановить пароль"')
    def test_click_recover_password_button(self, driver):
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)
        password_recover_page = RecoverPage(driver)

        header_page.click_user_account_button()
        account_page.click_password_recover_button()
        password_recover_page.click_recover_button()

        assert password_recover_page.find_element_save_button().is_displayed()

    @allure.title('Проверка перехода по кнопке "Восствноыить" после ввода почты')
    def test_click_recover_after_entering_email(self, driver,create_and_delete_user):
        password_recover_page = RecoverPage(driver)

        password_recover_page.open_page(Urls.forgot_password_page)
        password_recover_page.set_email_for_recover_password(create_and_delete_user[0]['email'])
        password_recover_page.click_recover_button()

        assert password_recover_page.find_element_save_button().is_displayed()

    @allure.title('Проверка поля "Пароль" при нажатии на иконку "глазок"')
    def test_active_password_field(self, driver, create_and_delete_user):
        password_recover_page = RecoverPage(driver)

        password_recover_page.open_page(Urls.forgot_password_page)
        password_recover_page.set_email_for_recover_password(create_and_delete_user[0]['email'])
        password_recover_page.click_recover_button()

        password_recover_page.find_element_save_button()
        password_recover_page.click_on_show_password_icon()

        assert password_recover_page.find_element_input_password_active