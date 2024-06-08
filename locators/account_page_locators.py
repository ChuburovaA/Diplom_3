from selenium.webdriver.common.by import By

class AccountPageLocators:
    # Страница входа
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'
    RESET_PASSWORD_BUTTON = By.XPATH, '//*[@href="/forgot-password"]'
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'

    # Личный кабинет
    PROFILE_BUTTON = By.XPATH, '//*[@href="/account/profile"]'  # профиль пользователя
    ORDERS_HISTORY_BUTTON = By.XPATH, '//*[@href="/account/order-history"]'  # история заказов
    ORDER_STATUS = By.XPATH, '//p[text()="Выполнен"]'  # статус заказа в истории
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'  # номер заказа в истории

    EXIT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'  # кнопка Выход