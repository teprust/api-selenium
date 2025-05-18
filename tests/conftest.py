import logging
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.add_login_form import AddLoginPage
from pages.model.registration_model import RegistrationModel

'''
Инициализация переменной логирования
'''
logger = logging.getLogger("logger_sel-api")

def pytest_addoption(parser):
    '''
    Функция настройки запуска
    '''
    parser.addoption("--url", action="store", default="http://158.160.87.146:5000", help="url")
    parser.addoption("--headless", action="store_true", help="url")

'''
Далее описываются фикстуры, выполняющиеся один раз при запуске тестов
'''

@pytest.fixture(scope="session")
def add_login_page(request):
    '''
    Функция создания драйвера и экземпляра класса AddLoginPage для работы с UI
    '''

    # Настройка и открытие страницы
    url = request.config.getoption('--url')
    is_headless = request.config.getoption('--headless')

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    if is_headless:
        chrome_options.add_argument("--headless=new")
    logger.info(f'Start app on url {url}? headless is {is_headless}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"{url}/login")

    # Экземпляр класса AddLoginPage
    add_login_page = AddLoginPage(driver)

    # yield алгоритм:
    # 1. передача экземпляра класса,
    # 2. выполнение действий вне данного метода,
    # 3. возврат к коду после yield.
    yield add_login_page
    logger.info(f'Stop tests')
    driver.quit()

@pytest.fixture(scope="session")
def register_admin(request, add_login_page):
    '''
    Функция регистрации нового администратора перед началом тестов
    :param add_login_page: экземпляр класса AddLoginPage для работы с UI
    '''

    body = RegistrationModel().random_admin()
    url = request.config.getoption("--url")
    response = requests.post(f"{url}/api/register", json=body)
    assert response.status_code == 200, f"Check register request, status code is {response.status_code}"

    logger.info(f'Success registration with login/password {body["login"]} {body["password"]}')

    register_admin = RegistrationModel(body["login"], body["password"])
    # Данные для авторизации администратора
    admin_data = {"login": register_admin.login, "password": register_admin.password}
    add_login_page.add_login_password(data=admin_data)

