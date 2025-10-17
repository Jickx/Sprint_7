import requests
from data.urls import CourierUrls


class CourierHelper:

    @staticmethod
    def create_courier(courier_data):
        return requests.post(CourierUrls.CREATE_COURIER, json=courier_data)

    @staticmethod
    def login_courier(credentials):
        return requests.post(CourierUrls.LOGIN_COURIER, json=credentials)

    @staticmethod
    def delete_courier(courier_data):
        login_response = CourierHelper.login_courier({
            'login': courier_data['login'],
            'password': courier_data['password']
        })

        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            return requests.delete(CourierUrls.DELETE_COURIER.format(courier_id=courier_id))
