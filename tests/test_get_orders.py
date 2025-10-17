from helpers.order_helper import OrderHelper


class TestGetOrders:

    def test_get_orders_returns_list(self):
        """Тест проверяет, что в теле ответа возвращается список заказов"""
        response = OrderHelper.get_orders()

        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        response_data = response.json()
        assert 'orders' in response_data, "В ответе отсутствует поле 'orders'"
        assert isinstance(response_data['orders'], list), "Поле 'orders' должно быть списком"

