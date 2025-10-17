import pytest
import allure
from helpers.courier_helper import CourierHelper
from data.courier_generator import CourierGenerator


@pytest.fixture
def courier():
    """Фикстура для создания тестового курьера"""
    with allure.step('Генерировать данные курьера'):
        courier_data = CourierGenerator.random_courier()
    with allure.step('Создать курьера'):
        response = CourierHelper.create_courier(courier_data)

    yield courier_data

    with allure.step('Удалить курьера после теста'):
        CourierHelper.delete_courier(courier_data)


@pytest.fixture
def courier_creds():
    """Фикстура для получения учетных данных курьера"""
    with allure.step('Сгенерировать учетные данные курьера'):
        courier_data = CourierGenerator.random_courier()
        credentials = {
            'login': courier_data['login'],
            'password': courier_data['password'],
            'firstName': courier_data.get('firstName')  # firstName не обязателен
        }
    return credentials


@pytest.fixture
def created_courier():
    """Фикстура для создания и последующего удаления курьера (для тестов авторизации)"""
    with allure.step('Генерировать данные курьера для логина'):
        courier_data = CourierGenerator.random_courier()
    with allure.step('Создать курьера для теста авторизации'):
        CourierHelper.create_courier(courier_data)

    yield courier_data

    with allure.step('Удалить курьера после теста авторизации'):
        CourierHelper.delete_courier(courier_data)
