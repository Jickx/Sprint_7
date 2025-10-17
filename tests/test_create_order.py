import pytest
import allure
from helpers.order_helper import OrderHelper
from data.order_generator import OrderGenerator


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @allure.description('Проверка: один цвет (BLACK/GREY), оба цвета или без цвета; в ответе есть track')
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
        with allure.step(f'Сгенерировать данные заказа (color={color})'):
            order_data = OrderGenerator.random_order(color=color)

        with allure.step('Отправить запрос на создание заказа'):
            response = OrderHelper.create_order(order_data)

        with allure.step('Проверить код ответа 201'):
            assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"

        with allure.step("Проверить, что в ответе есть поле 'track' (int)"):
            body = response.json()
            assert 'track' in body, "В ответе отсутствует поле 'track'"
            assert isinstance(body['track'], int), "Поле 'track' должно быть числом"
            track_number = body['track']

        with allure.step(f'Отменить заказ (track={track_number})'):
            OrderHelper.cancel_order(track_number)
