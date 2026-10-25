import allure
from orders_api import OrdersApi


@allure.feature('Заказы: список заказов')
class TestGetOrders:

    @allure.title('В теле ответа возвращается список заказов')
    @allure.description('Запрос списка заказов с параметрами limit и page. В ответе приходит 200 и список orders')
    def test_get_orders_list_returns_orders(self):
        response = OrdersApi.get_orders_list({'limit': 10, 'page': 0})

        assert response.status_code == 200, response.text
        body = response.json()
        assert 'orders' in body, f'В ответе нет ключа orders: {body}'
        assert isinstance(body['orders'], list), f'orders не список: {type(body["orders"])}'