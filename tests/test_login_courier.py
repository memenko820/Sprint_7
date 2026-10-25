import allure
import pytest
import requests
import data
import helpers
from courier_api import CourierApi


@allure.feature('Курьер: авторизация')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_login_courier_success(self, courier):
        response = CourierApi.login(helpers.get_credentials(courier))

        assert response.status_code == 200, response.text
        assert 'id' in response.json()
        assert isinstance(response.json()['id'], int)

    @allure.title('Система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize('wrong_field', [
        pytest.param('login', id='неправильный логин'),
        pytest.param('password', id='неправильный пароль'),
    ])
    def test_login_courier_with_wrong_credentials_returns_not_found(self, courier, wrong_field):
        payload = {**helpers.get_credentials(courier), wrong_field: helpers.generate_random_string(10)}
        response = CourierApi.login(payload)

        assert response.status_code == 404, response.text
        assert response.json() == data.LOGIN_COURIER_ERROR_WRONG_DATA

    @allure.title('Запрос на авторизацию возвращает ошибку, если нет одного из полей')
    @allure.description('Курьер создан. В теле запроса на авторизацию не хватает логина или пароля')
    @pytest.mark.parametrize('missing_field', [
        pytest.param('login', id='без логина'),
        pytest.param('password', id='без пароля', marks=pytest.mark.xfail(
            raises=requests.exceptions.ReadTimeout,
            reason='Баг сервиса: запрос авторизации без пароля зависает и через ~2 минуты возвращает 504 вместо 400'
        )),
    ])
    def test_login_courier_without_required_field_returns_bad_request(self, courier, missing_field):
        credentials = helpers.get_credentials(courier)
        payload = {key: value for key, value in credentials.items() if key != missing_field}
        response = CourierApi.login(payload)

        assert response.status_code == 400, response.text
        assert response.json() == data.LOGIN_COURIER_ERROR_NOT_ENOUGH_DATA_MESSAGE

    @allure.title('Авторизация под несуществующим пользователем возвращает ошибку')
    @allure.description('Курьер не зарегистрирован в системе и пытается авторизоваться')
    def test_login_courier_with_unregistered_data_returns_not_found(self, new_courier_payload):
        response = CourierApi.login(helpers.get_credentials(new_courier_payload))

        assert response.status_code == 404, response.text
        assert response.json() == data.LOGIN_COURIER_ERROR_WRONG_DATA