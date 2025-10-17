import pytest
from http import HTTPStatus
from data.courier_generator import CourierGenerator
from helpers.courier_helper import CourierHelper
from data.messages import INSUFFICIENT_DATA_MESSAGE, LOGIN_ALREADY_EXISTS_MESSAGE


class TestCourierCreation:

    def test_create_courier_success(self, courier_creds):
        response = CourierHelper.create_courier(courier_creds)

        assert response.status_code == HTTPStatus.CREATED
        assert response.json()['ok'] is True

    def test_create_duplicate_courier(self, courier):
        response = CourierHelper.create_courier(courier)

        assert response.status_code == HTTPStatus.CONFLICT
        assert response.json().get('message') == LOGIN_ALREADY_EXISTS_MESSAGE

    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_required_field(self, courier_creds, missing_field):
        courier_data = dict(courier_creds)
        courier_data.pop(missing_field, None)
        response = CourierHelper.create_courier(courier_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json().get('message') == INSUFFICIENT_DATA_MESSAGE

    def test_create_courier_existing_login(self, courier):
        new_courier = CourierGenerator.random_courier()
        new_courier['login'] = courier['login']

        response = CourierHelper.create_courier(new_courier)
        assert response.status_code == HTTPStatus.CONFLICT
        assert response.json().get('message') == LOGIN_ALREADY_EXISTS_MESSAGE
