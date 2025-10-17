import pytest
from http import HTTPStatus
from helpers.courier_helper import CourierHelper
from data.courier_generator import CourierGenerator
from data.messages import ACCOUNT_NOT_FOUND_MESSAGE, INSUFFICIENT_LOGIN_DATA_MESSAGE


class TestCourierLogin:

    def test_courier_can_login(self, created_courier):
        """Курьер может авторизоваться"""
        credentials = {
            'login': created_courier['login'],
            'password': created_courier['password']
        }
        response = CourierHelper.login_courier(credentials)

        assert response.status_code == HTTPStatus.OK
        assert 'id' in response.json()
        assert isinstance(response.json()['id'], int)

    def test_login_returns_courier_id(self, created_courier):
        """Успешный запрос возвращает id"""
        credentials = {
            'login': created_courier['login'],
            'password': created_courier['password']
        }
        response = CourierHelper.login_courier(credentials)

        assert response.status_code == HTTPStatus.OK
        response_data = response.json()
        assert 'id' in response_data
        assert response_data['id'] is not None

    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_login_missing_required_field(self, created_courier, missing_field):
        """Если какого-то поля нет, запрос возвращает ошибку"""
        credentials = {
            'login': created_courier['login'],
            'password': created_courier['password']
        }
        credentials.pop(missing_field, None)

        response = CourierHelper.login_courier(credentials)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json().get('message') == INSUFFICIENT_LOGIN_DATA_MESSAGE

    def test_login_with_wrong_password(self, created_courier):
        """Система вернёт ошибку, если неправильно указать пароль"""
        credentials = {
            'login': created_courier['login'],
            'password': 'wrong_password_123'
        }
        response = CourierHelper.login_courier(credentials)

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json().get('message') == ACCOUNT_NOT_FOUND_MESSAGE

    def test_login_with_wrong_login(self, created_courier):
        """Система вернёт ошибку, если неправильно указать логин"""
        credentials = {
            'login': 'wrong_user_12345',
            'password': created_courier['password']
        }
        response = CourierHelper.login_courier(credentials)

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json().get('message') == ACCOUNT_NOT_FOUND_MESSAGE

    def test_login_nonexistent_user(self):
        """Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку"""
        fake_courier = CourierGenerator.random_courier()
        credentials = {
            'login': fake_courier['login'],
            'password': fake_courier['password']
        }
        response = CourierHelper.login_courier(credentials)

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json().get('message') == ACCOUNT_NOT_FOUND_MESSAGE
