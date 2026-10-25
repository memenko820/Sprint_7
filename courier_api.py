import allure
import requests
import data
import helpers


class CourierApi:

    @staticmethod
    @allure.step('Создание курьера')
    def create(payload):
        return requests.post(f'{data.BASE_URL}{data.COURIER_CREATE_PATH}', data=payload, timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Логин курьера в системе')
    def login(payload):
        return requests.post(f'{data.BASE_URL}{data.COURIER_LOGIN_PATH}', data=payload, timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Удаление курьера из системы')
    def delete(courier_id):
        return requests.delete(f'{data.BASE_URL}{data.COURIER_DELETE_PATH}/{courier_id}', timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Регистрация нового курьера')
    def register_new_courier_and_return_login_password(): 
        payload = helpers.generate_courier_payload()
        response = CourierApi.create(payload)

        if response.status_code == 201:
            return [payload['login'], payload['password'], payload['firstName']]
        return []

    @staticmethod
    @allure.step('Удаление курьера по логину и паролю')
    def delete_by_credentials(login, password):        
        login_response = CourierApi.login({'login': login, 'password': password})

        if login_response.status_code == 200:
            CourierApi.delete(login_response.json()['id'])

    