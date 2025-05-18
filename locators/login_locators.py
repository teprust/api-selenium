from selenium.webdriver.common.by import By


class LoginLocators:
    '''
    Локаторы для работы с формой входа администратора

    LOGIN - локатор для поиска поля "Email / Логин"
    PASSWORD - локатор для поиска поля "Пароль"
    LOGIN_BUTTON - локатор для поиска кнопки "Войти"
    TO_ADD_USER - локатор для поиска кнопки меню "Добавить пользователя"

    '''

    LOGIN = (By.XPATH, '//input[@name="login"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    LOGIN_BUTTON = (By.ID, 'add-btn')
    TO_ADD_USER = (By.XPATH, '//a[@href="/add-user"]')
