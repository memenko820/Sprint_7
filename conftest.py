import pytest
import helpers
from courier_api import CourierApi
from orders_api import OrdersApi


@pytest.fixture
# Подготовка данных для создания курьера
def new_courier_payload():
    payload = helpers.generate_courier_payload()

    yield payload

    _delete_courier(payload['login'], payload['password'])


@pytest.fixture
# Уже созданный курьер до теста, для логинов и дубликатов
def courier():
    login_pass = helpers.register_new_courier_and_return_login_password()
    assert login_pass, 'Предусловие не выполнено: не удалось зарегистрировать курьера'

    login, password, first_name = login_pass

    payload = {
        'login': login,
        'password': password,
        'firstName': first_name,
        }

    yield payload

    # Постусловие: удаляем курьера после теста
    _delete_courier(payload['login'], payload['password'])

# метод для постусловия: удаляет зарегистрированного курьера
def _delete_courier(login, password):
    login_response = CourierApi.login({'login': login, 'password': password})
    if login_response.status_code == 200:
        delete_response = CourierApi.delete(login_response.json()['id'])
        assert delete_response.status_code == 200, f'Курьер не удалён: {delete_response.text}'

@pytest.fixture
# Фикстура для удаления созданных списков с заказами. Фикстура отдаёт пустой список, тест наполняет список заказами, после чего фикстура удаляет заказы
def orders_to_cancel():
    tracks = []
    yield tracks
    for track in tracks:
        response = OrdersApi.cancel(track)
        assert response.status_code == 200, f'Заказ {track} не отменён: {response.text}'