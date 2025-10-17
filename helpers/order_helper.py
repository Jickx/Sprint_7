import requests
from data.urls import OrderUrls


class OrderHelper:

    @staticmethod
    def create_order(order_data):
        return requests.post(OrderUrls.CREATE_ORDER, json=order_data)

    @staticmethod
    def get_orders():
        return requests.get(OrderUrls.GET_ORDERS)
