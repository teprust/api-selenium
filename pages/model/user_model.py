from faker import Faker

'''
Инициализация переменной для работы с библиотекой Faker
'''
fake = Faker("ru_RU")

class UserModel:
    '''
    Класс для работы с данными добавляемого пользователя
    '''
    def __init__(self, name=None, age=None, gender=None, date=None, status=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.date = date
        self.status = status


    def random_user(self):
        '''
        Функция создания случайных данных для нового студента
        с помощью библиотеки Faker

        :return: словарь, состоящий из имени, возраста, пола, даты регистрации и статуса обучения
         нового студента
        '''

        name = fake.name()
        age = fake.random_int(0, 150)
        gender = fake.random_element(elements=("М", "Ж"))
        date = fake.date(pattern='%d.%m.%Y')
        status = fake.boolean()

        return {"name": name, "age": age, "gender": gender, "date": date, "status": status}