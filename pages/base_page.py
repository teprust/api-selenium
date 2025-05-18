from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator, wait_time=10):
        '''
        Поиск элемента на веб-странице, с ожиданием загрузки (внутренний метод)
        :param locator: аналогичен (By.ID, 'username')
        :param wait_time: время задержки на поиск элемента
        :return: возвращает объект selenium
        '''

        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"ErrLoc: can't find element by locator {locator}",
        )
        return element

    def _find_element_for_add_form(self, locator_success, locator_error_name, locator_error_age, wait_time=10):
        '''
        Поиск нескольких элементов на веб-странице, с ожиданием загрузки (внутренний метод)
        :param locator_success - локатор для поиска сообщения "Пользователь успешно авторизован!"
        :param locator_error_name - локатор для поиска сообщения "Поле обязательно" для поля "Имя"
        :param locator_error_age - локатор для поиска сообщения "Поле обязательно" для поля "Возраст"
        :param wait_time: время задержки на поиск элемента
        :return: возвращает объект selenium
        '''

        element = WebDriverWait(self.driver, wait_time).until(
            EC.any_of(
                EC.visibility_of_element_located(locator_success),
                EC.visibility_of_element_located(locator_error_name),
                EC.visibility_of_element_located(locator_error_age),
            )
        )
        return element

    def click(self, locator, wait_time=10):
        '''
        Нажатие кнопки
        :param locator: аналогичен (By.ID, 'username')
        :param wait_time: время задержки на поиск элемента
        '''

        element = self._find_element(locator, wait_time)
        element.click()

    def fill(self, value: str, locator, wait_time=60):
        '''
        fill = send_keys - т.е. заполнение текстового поля
        :param value: строка, которая будет добавлена в поле
        :param locator: аналогичен (By.ID, 'username')
        :param wait_time: время задержки на поиск элемента
        '''

        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator_success, locator_error_name, locator_error_age, wait_time=20) -> str:
        '''
        Функция получения сообщения о результате добавления новго студента
        :param locator_success - локатор для поиска сообщения "Пользователь успешно авторизован!"
        :param locator_error_name - локатор для поиска сообщения "Поле обязательно" для поля "Имя"
        :param locator_error_age - локатор для поиска сообщения "Поле обязательно" для поля "Возраст"
        :param wait_time: время задержки на поиск элемента
        :return: текст ошибки или удачи (для нашего приложения - текст в одном из полей вывода)
        '''

        element = self._find_element_for_add_form(locator_success, locator_error_name, locator_error_age, wait_time)
        return element.text

    def url_check(self, wait_time=10)-> bool:
        '''
        Функция проверки перехода на страницу со списком пользователей
        после успешного входа администратора
        :param wait_time: время задержки на поиск элемента
        :return: True - успешно перешли к странице просмотра студентов, False - иначе
        '''

        element = WebDriverWait(self.driver, wait_time).until(EC.url_contains("/users-page"))
        if element:
            return True
        else:
            return False

    def cleaner(self, locators, wait_time=10):
        '''

        :param locators: локаторы полей и чекбокса, которые необходимо очистить
        :param wait_time: время задержки на поиск элемента
        '''

        self._find_element(locators["0"], wait_time).clear()
        self._find_element(locators["1"], wait_time).clear()
        self._find_element(locators["2"], wait_time).clear()
        self._find_element(locators["3"], wait_time).clear()

        # Чекбокс можно очистить только в случае, если он был выбран
        checkbox = self._find_element(locators["4"], wait_time)
        if checkbox.is_selected():
            checkbox.clear()