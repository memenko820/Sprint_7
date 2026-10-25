import allure
import requests
import data


class CourierApi:

    @staticmethod
    @allure.step('Создание курьера')
    def create(payload):
        return requests.post(f'{data.BASE_URL}{data.COURIER_CREATE_PATH}', data=payload, timeout=10)

    @staticmethod
    @allure.step('Логин курьера в системе')
    def login(payload):
        return requests.post(f'{data.BASE_URL}{data.COURIER_LOGIN_PATH}', data=payload, timeout=10)

    @staticmethod
    @allure.step('Удаление курьера из системы')
    def delete(courier_id):
        return requests.delete(f'{data.BASE_URL}{data.COURIER_DELETE_PATH}/{courier_id}', timeout=10)

    