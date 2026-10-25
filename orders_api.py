import allure
import requests
import data


class OrdersApi:

    @staticmethod
    @allure.step('Создание заказа')
    def create(payload):
        return requests.post(f'{data.BASE_URL}{data.ORDER_CREATE_PATH}', json=payload, timeout=10)

    @staticmethod
    @allure.step('Отмена созданного заказа')
    def cancel(track):
        return requests.put(f'{data.BASE_URL}{data.ORDER_CANCEL_PATH}', params={'track': track}, timeout=10)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders_list(params=None):
        return requests.get(f'{data.BASE_URL}{data.ORDER_LIST_PATH}', params=params, timeout=10)