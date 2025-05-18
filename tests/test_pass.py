from pages.model.user_model import UserModel

class TestAddUser:
    '''
    Класс для выполнения тестов
    '''
    def test_happy_path_1(self, register_admin, add_login_page):
        '''
        Тест 1. Проверка добавления корректного пользователя с наличием всех полей
        '''

        user_data = UserModel().random_user()
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        assert "Пользователь успешно добавлен!" in result_user, "Ошибка добавления пользователя"


    def test_happy_path_2(self, register_admin, add_login_page):
        '''
        Тест 2. Проверка добавления корректного пользователя с наличием только обязательных полей
        '''

        user_data = UserModel().random_user()
        user_data["date"]= None
        user_data["status"] = None
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        assert "Пользователь успешно добавлен!" in result_user, "Ошибка добавления пользователя"

    def test_happy_path_3(self, register_admin, add_login_page):
        '''
        Тест 3. Проверка добавления корректного пользователя с наличием всех полей, кроме чекбокса статуса обучения
        '''

        user_data = UserModel().random_user()
        user_data["status"] = None
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        assert "Пользователь успешно добавлен!" in result_user, "Ошибка добавления пользователя"

    def test_unhappy_path_1(self, register_admin, add_login_page):
        '''
        Тест 4. Проверка добавления пользователя без заполнения поля "Имя"
        '''

        user_data = UserModel().random_user()
        user_data["name"] = None
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        add_login_page.clean_form()
        assert "Поле обязательно" in result_user, "Ошибочное добавление пользователя"

    def test_unhappy_path_2(self, register_admin, add_login_page):
        '''
        Тест 5. Проверка добавления пользователя без заполнения поля "Возраст"
        '''

        user_data = UserModel().random_user()
        user_data["age"] = None
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        add_login_page.clean_form()
        assert "Поле обязательно" in result_user, "Ошибочное добавление пользователя"

    def test_unhappy_path_3(self, register_admin, add_login_page):
        '''
        Тест 6. Проверка добавления пользователя без заполнения полей "Имя" и "Возраст"
        '''

        user_data = UserModel().random_user()
        user_data["name"] = None
        user_data["age"] = None
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        add_login_page.clean_form()
        assert "Поле обязательно" in result_user, "Ошибочное добавление пользователя"