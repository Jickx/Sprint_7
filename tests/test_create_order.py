import pytest
from helpers.order_helper import OrderHelper
from data.order_generator import OrderGenerator


class TestCreateOrder:

    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            None,
        ]
    )
    def test_create_order_with_different_colors(self, color):
        """Тест создания заказа с разными вариантами цвета"""
        order_data = OrderGenerator.random_order(color=color)

        response = OrderHelper.create_order(order_data)

        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        assert 'track' in response.json(), "В ответе отсутствует поле 'track'"
        assert isinstance(response.json()['track'], int), "Поле 'track' должно быть числом"
