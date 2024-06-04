from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Лента заказов
    ORDERS_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'

    ORDER_IN_WORK_NUMBER = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'
    ALL_ORDERS_READY_TEXT = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'
    COMPLETED_ORDERS_TOTAL = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'
    COMPLETED_ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'

    # Детали заказа
    ORDER_STRUCTURE_TITLE = By.XPATH, '//p[text()="Cостав"]'
    ORDER_NUMBER = By.XPATH, '//p[text()="{}"]'

