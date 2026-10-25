import pytest
import allure
from courier_api import CourierApi
import helpers
import data

@allure.feature('Курьер: создание в системе')
class TestCreateCourier:

    @allure.title('Можно создать курьера в системе')
    @allure.description('Отправка POST-запроса на создание курьера с валидными данными и получение сообщения об успешном создании курьера в системе с соответствующим статус-кодом и тексте сообщения в теле ответа')
    def test_create_courier_success(self, new_courier_payload):
        response = CourierApi.create(new_courier_payload)

        assert response.status_code == 201, response.text
        assert response.json() == data.CREATE_COURIER_SUCCESS_RESPONSE

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('Отправка POST-запроса на создание курьера в системе с идентичными данными, которые уже есть в системе с целью получить соответствующую ошибку')
    def test_create_courier_with_existing_payload_error(self, courier):
        response = CourierApi.create(courier)
        
        assert response.status_code == 409
        assert response.json() == data.CREATE_COURIER_ERROR_EXISTING_LOGIN_MESSAGE

    @allure.title('Запрос возвращает ошибку, если нет одного из полей')
    @allure.description('Отправка POST-запроса на создание курьера в системе при отсутствующем обязательном поле в теле запроса с целью проверки соответствующей ошибки')
    @pytest.mark.parametrize('missing_field', [
        pytest.param('login', id='без логина'),
        pytest.param('password', id='без пароля'),
    ])
    def test_create_courier_without_required_field_error(self, new_courier_payload, missing_field):
        payload = helpers.remove_field(new_courier_payload, missing_field)
        response = CourierApi.create(payload)

        assert response.status_code == 400
        assert response.json() == data.CREATE_COURIER_ERROR_NOT_ENOUGH_DATA_MESSAGE

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка')
    @allure.description('Отправка POST-запроса на создание курьера в системе с идентичным логином курьера, который уже создан в системе, остальные данные при этом отличаются')
    def test_create_courier_with_existing_login_returns_conflict(self, courier):
        payload = {**courier, 'password': helpers.generate_random_string(10), 'firstName': helpers.generate_random_string(10)}
        response = CourierApi.create(payload)

        assert response.status_code == 409
        assert response.json() == data.CREATE_COURIER_ERROR_EXISTING_LOGIN_MESSAGE
