import pytest
import requests
from selenium import webdriver

from data import Urls
from helpers import *

from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.account_page import AccountPage

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.get(Urls.BASE_PAGE)

    yield driver
    driver.quit()

@pytest.fixture
def create_user_data():
    name = generate_random_string(6)
    email = generate_random_string(6) + '@yandex.ru'
    password = generate_random_string(6)
    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    return payload


@pytest.fixture(scope="function")
def create_and_delete_user(create_user_data):
    payload = create_user_data
    login_data = payload.copy()
    del login_data["name"]

    response = requests.post(Urls.register_user, data=payload)
    token = response.json()["accessToken"]

    yield login_data, token, payload
    requests.delete(Urls.delete_user, headers={'Authorization': f'{token}'})


@pytest.fixture
def login_user(driver, create_and_delete_user):
    main_page = MainPage(driver)
    header_page = HeaderPage(driver)
    account_page = AccountPage(driver)

    main_page.click_on_enter_button()
    header_page.click_user_account_button()

    account_page.input_text_email(create_and_delete_user)
    account_page.input_text_password(create_and_delete_user)
    account_page.click_to_enter_button()


