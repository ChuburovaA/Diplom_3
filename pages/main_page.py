import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_enter_button(self):
        self.move_to_element_and_click(MainPageLocators.ENTERANCE_BUTTON)
    @allure.step('Проверка заголовка "Соберите бургер"')
    def wait_visibility_element_burger_constructor_title(self):
        self.wait_visibility_element(MainPageLocators.CONSTRUCTOR_BURGER)

    @allure.step('Клик по ингредиенту "Флюоресцентная булка"')
    def click_on_bun(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Получение заголовка всплывающего окна "Детали ингредиента"')
    def check_counter_of_detail_popup(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_DETAIL_POPUP_TITLE)

    @allure.step('Клик по крестику в модальном окне')
    def click_close_button(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Добавление булки в корзину')
    def add_bun_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавление начинки в корзину')
    def add_filling_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавление соуса в корзину')
    def add_sauce_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получение номера заказа"')
    def find_element_order_number_text(self):
        return self.find_element(MainPageLocators.ORDER_NUMBER_TEXT)

    @allure.step('Проверка сообщения "Ваш заказ начали готовить"')
    def check_element_order_status(self):
        return self.check_element(MainPageLocators.ORDER_STATUS)

    @allure.step('Получение количества добавленного ингредиента')
    def check_counter_of_ingredients(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Создание заказа и получение его номера')
    def make_order_and_get_order_number(self):
        self.wait_visibility_element(MainPageLocators.INGREDIENT_BUN)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        self.find_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_visibility_element(MainPageLocators.ORDER_STATUS)
        self.wait_invisibility_element(MainPageLocators.DEFAULT_ORDER_NUMBER)
        order = self.get_text_of_element(MainPageLocators.ORDER_NUMBER_TEXT)
        self.move_to_element_and_click(MainPageLocators.CLOSE_BUTTON)
        return order

    @allure.step('Проверка отображения текста счетчика ингредиента')
    def check_text_of_ingredients_counter(self):
        return self. check_invisibility(MainPageLocators.INGREDIENT_DETAIL_POPUP)

    @allure.step('Получение ингредиента "Булочка"')
    def find_element_ingredient_bun(self):
        return self.find_element(MainPageLocators.INGREDIENT_BUN)