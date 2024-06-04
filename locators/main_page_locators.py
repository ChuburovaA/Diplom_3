from selenium.webdriver.common.by import By

class MainPageLocators:
    # Стартовая страница
    ENTERANCE_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'

    CONSTRUCTOR_BURGER = By.XPATH, '//h1[text()="Соберите бургер"]'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]'

    # Ингрединты
    INGREDIENT_BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'  # "Флюоресцентная булка R2-D3"
    INGREDIENT_SAUCE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]'  # "Соус Spicy-X"
    INGREDIENT_FILLING = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]' # "Мясо бессмертных моллюсков Protostomia"
    INGREDIENT_COUNTER = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]//p[contains(@class, "counter__num")]'

    # Детали ингредиента
    INGREDIENT_DETAIL_POPUP_TITLE = By.XPATH, '//h2[text()="Детали ингредиента"]'
    INGREDIENT_DETAIL_POPUP = By.XPATH, '//*[contains(@class, "contentBox")]'

    # Всплывающее окно с номером заказа
    ORDER_NUMBER_TEXT = By.XPATH, '//*[contains(@class, "type_digits-large")]'
    DEFAULT_ORDER_NUMBER = By.XPATH, '//h2[text()="9999"]'
    ORDER_STATUS = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'
    CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]'



