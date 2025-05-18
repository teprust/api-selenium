from selenium.webdriver.common.by import By

class UserLocators:
    '''
    Локаторы для работы с формой добавления пользователей

    NAME - локатор для поиска поля "Имя"
    AGE - локатор для поиска поля "Возраст"
    GENDER - локатор для поиска поля "Пол"
    DATE - локатор для поиска поля "Дата регистрации"
    STATUS - локатор для поиска чекбокса "Статус обучения студента"
    MESSAGE - локатор для поиска текста успешного добавления студента
    ERROR_AGE - локатор для поиска текста ошибки добавления студента без имени
    ERROR_NAME - локатор для поиска текста ошибки добавления студента без возраста
    '''

    NAME = (By.ID, "name")
    AGE = (By.ID, "age")
    GENDER = (By.ID, "gender")
    DATE = (By.ID, "date_birthday")
    STATUS = (By.ID, "isActive")
    SAVE_BUTTON = (By.ID, 'add-btn')
    MESSAGE = (By.XPATH, '//div[@class="alert alert-success"]')
    ERROR_AGE = (By.ID, 'ageError')
    ERROR_NAME = (By.ID, 'nameError')
