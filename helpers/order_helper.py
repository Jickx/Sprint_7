import requests
import allure
from data.urls import OrderUrls


class OrderHelper:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order_data):
        with allure.step('POST /api/v1/orders'):
            return requests.post(OrderUrls.CREATE_ORDER, json=order_data)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders():
        with allure.step('GET /api/v1/orders'):
            return requests.get(OrderUrls.GET_ORDERS)
