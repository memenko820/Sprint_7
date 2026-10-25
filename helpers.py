import requests
import random
import string
import data
from datetime import date, timedelta

# метод регистрации нового курьера возвращает список из логина, пароля и имени
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    payload = generate_courier_payload()

    response = requests.post(f'{data.BASE_URL}{data.COURIER_CREATE_PATH}', data=payload, timeout=10)

    if response.status_code == 201:
        return [payload['login'], payload['password'], payload['firstName']]

    return []

# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

# Генерация данных для курьера
def generate_courier_payload():
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10)
        }

# Генерация данных для заказа с опциональным цветом самоката
def generate_order_payload(colors=None):
    payload = {
        'firstName': generate_random_string(10),
        'lastName': generate_random_string(10),
        'address': 'Konoha, 142 apt.',
        'metroStation': '4',
        'phone': '+7 800 355 35 35',
        'rentTime': 5,
        'deliveryDate': (date.today() + timedelta(days=1)).isoformat(),
        'comment': generate_random_string(15),
    }
    if colors is not None:
        payload['color'] = colors
    return payload

# Собирает тело для авторизации курьера без поля firstName
def get_credentials(courier_data):
    return {'login': courier_data['login'], 'password': courier_data['password']}