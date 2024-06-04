from selenium.webdriver.common.by import By

class HeaderPageLocators:
    ACCOUNT_BUTTON = By.XPATH, '//*[@href="/account"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    ORDERS_LIST_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'