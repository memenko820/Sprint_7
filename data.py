# Базовый URL сервиса Яндекс.Самокат
BASE_URL = 'https://qa-scooter.education-services.ru'

# Пути ручек:
# Создание курьера
COURIER_CREATE_PATH = '/api/v1/courier'
# Авторизация курьера в системе
COURIER_LOGIN_PATH = '/api/v1/courier/login'
# Удаление курьера
COURIER_DELETE_PATH = '/api/v1/courier'
# Создание заказа
ORDER_CREATE_PATH = '/api/v1/orders'
# Отменить заказ
ORDER_CANCEL_PATH = '/api/v1/orders/cancel'
# Список заказов
ORDER_LIST_PATH = '/api/v1/orders'

# Тексты сообщений и body-ответов:
# Курьер успешно зарегистрирован в системе
CREATE_COURIER_SUCCESS_RESPONSE = {'ok': True}
# Запрос без логина или пароля
CREATE_COURIER_ERROR_NOT_ENOUGH_DATA_MESSAGE = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
# Запрос с повторяющимся логином
CREATE_COURIER_ERROR_EXISTING_LOGIN_MESSAGE = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

# Логин курьера с несуществующей парой логин-пароль:
LOGIN_COURIER_ERROR_WRONG_DATA = {'code': 404, 'message': 'Учетная запись не найдена'}
# Логин курьера без логина или пароля
LOGIN_COURIER_ERROR_NOT_ENOUGH_DATA_MESSAGE = {'code': 400, 'message': 'Недостаточно данных для входа'}

# Таймаут запросов к сервису, секунды
REQUEST_TIMEOUT = 30