import pytest
import helpers
from courier_api import CourierApi
from orders_api import OrdersApi


@pytest.fixture
# Подготовка данных для создания курьера
def new_courier_payload():
    payload = helpers.generate_courier_payload()

    yield payload

    CourierApi.delete_by_credentials(payload['login'], payload['password'])

@pytest.fixture
# Уже созданный курьер до теста, для логинов и дубликатов
def courier():
    login, password, first_name = CourierApi.register_new_courier_and_return_login_password()
    
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name,
        }

    yield payload

    # Постусловие: удаляем курьера после теста
    CourierApi.delete_by_credentials(payload['login'], payload['password'])

@pytest.fixture
def created_orders():
    responses = []

    yield responses

    for response in responses:
        track = response.json().get('track')
        if track is not None:
            OrdersApi.cancel(track)