import allure
from helpers.order_helper import OrderHelper


@allure.feature('Получение списка заказов')
class TestGetOrders:

    @allure.title('В теле ответа возвращается список заказов')
    @allure.description('Проверка, что эндпоинт возвращает список заказов в поле orders')
    def test_get_orders_returns_list(self):
        """Тест проверяет, что в теле ответа возвращается список заказов"""
        with allure.step('Отправить запрос на получение списка заказов'):
            response = OrderHelper.get_orders()

        with allure.step('Проверить код ответа 200'):
            assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"

        with allure.step('Проверить, что поле orders присутствует и это список'):
            response_data = response.json()
            assert 'orders' in response_data, "В ответе отсутствует поле 'orders'"
            assert isinstance(response_data['orders'], list), "Поле 'orders' должно быть списком"
