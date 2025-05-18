import logging
from locators.add_user_locators import UserLocators
from locators.login_locators import LoginLocators
from pages.base_page import BasePage

'''
Инициализация переменной логирования
'''
logger = logging.getLogger("logger_sel-api")

class AddLoginPage(BasePage):
    '''
    Класс для работы с UI страниц входа и добавления нового пользователя
    '''

    def __init__(self, driver):
        super().__init__(driver)

    def add_login_password(self, data: dict):
        '''
        Функция входа администратора в систему
        :param data: словарь, состоящий из логина и пароля администратора
        '''
        # Заполняем поля по локаторам
        self.fill(value=data["login"], locator=LoginLocators.LOGIN)
        self.fill(value=data["password"], locator=LoginLocators.PASSWORD)

        logger.info(f'Try to login with username {data["login"]}')
        logger.info(f'Try to login with password {data["password"]}')

        # Нажатие на кнопку по локатору
        self.click(locator=LoginLocators.LOGIN_BUTTON)

        # Проверяем успешность авторизации по обновлению адреса на страницу
        # со списком пользователей
        if self.url_check():
            logger.info('OK authentication!')
            self.click(locator=LoginLocators.TO_ADD_USER)


    def add_user_info(self, data: dict):
        '''
        Функция добавления нового студента
        :param data: словарь, состоящий из имени, возраста, пола, даты регистрации
        и статуса обучения нового студента
        '''

        # Заполняем поля по локатору
        self.fill(value=data["name"], locator=UserLocators.NAME)
        self.fill(value=data["age"], locator=UserLocators.AGE)
        self.fill(value=data["gender"], locator=UserLocators.GENDER)
        self.fill(value=data["date"], locator=UserLocators.DATE)
        self.fill(value=data["status"], locator=UserLocators.STATUS)

        logger.info(f'Try to add user with name {data["name"]}')
        logger.info(f'Try to add user with age {data["age"]}')
        logger.info(f'Try to add user with gender {data["gender"]}')
        logger.info(f'Try to add user with date {data["date"]}')
        logger.info(f'Try to add user with status {data["status"]}')

        # Нажатие на кнопку по локатору
        self.click(locator=UserLocators.SAVE_BUTTON)

    def get_add_result(self):
        '''
        Функция получения результата операции добавления нового студента
        :return: возвращает текст результата добавления
        '''
        return self.text(UserLocators.MESSAGE, UserLocators.ERROR_NAME, UserLocators.ERROR_AGE)

    def clean_form(self):
        '''
        Функция очистки формы добавления студента по лоакторам полей
        '''
        locators={
            '0': UserLocators.NAME,
            '1': UserLocators.AGE,
            '2': UserLocators.GENDER,
            '3': UserLocators.DATE,
            '4': UserLocators.STATUS,
        }
        self.cleaner(locators)
        logger.info('Clean form')