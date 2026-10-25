import allure
import pytest
import helpers
from orders_api import OrdersApi


@allure.feature('Заказы: создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа на аренду самоката с разным выбором цвета')
    @allure.description('Тело запроса валидно, меняется только поле color. В ответе приходит 201 и track заказа')
    @pytest.mark.parametrize('colors', [
        pytest.param(['BLACK'], id='чёрный'),
        pytest.param(['GREY'], id='серый'),
        pytest.param(['BLACK', 'GREY'], id='оба цвета'),
        pytest.param(None, id='без цвета'),
    ])
    def test_create_order_with_colors_returns_track(self, colors, created_orders):
        response = OrdersApi.create(helpers.generate_order_payload(colors))
        created_orders.append(response)

        assert response.status_code == 201, response.text
        body = response.json()
        assert 'track' in body, f'В ответе нет track: {body}'
        assert isinstance(body['track'], int)