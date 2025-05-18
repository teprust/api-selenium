from faker import Faker

'''
Инициализация переменной для работы с библиотекой Faker
'''
fake = Faker("ru_RU")


class RegistrationModel:
    '''
    Класс для работы с данными администратора
    '''
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def random_admin(self):
        '''
        Функция создания случайных логина и пароля для нового администратора
        с помощью библиотеки Faker

        :return: словарь, состоящий из логина и пароля для нового администратора
        '''
        return {"login": fake.user_name(), "password": fake.password()}
