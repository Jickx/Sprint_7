import pytest
from helpers.courier_helper import CourierHelper
from data.courier_generator import CourierGenerator


@pytest.fixture
def courier():
    """Фикстура для создания тестового курьера"""
    courier_data = CourierGenerator.random_courier()
    response = CourierHelper.create_courier(courier_data)

    yield courier_data

    CourierHelper.delete_courier(courier_data)


@pytest.fixture
def courier_creds():
    """Фикстура для получения учетных данных курьера"""
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
    courier_data = CourierGenerator.random_courier()
    CourierHelper.create_courier(courier_data)

    yield courier_data

    CourierHelper.delete_courier(courier_data)

