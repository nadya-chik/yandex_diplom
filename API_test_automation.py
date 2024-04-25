# Надежда Чикишева, 15-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import data
import requests

# Функция для создания заказа и сохранения трек-номера заказа
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
track_number = post_create_order(data.order_body).json()["track"]
# Функция для получения заказа по трек-номеру
def get_order_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER + str(track_number))
response = get_order_number(track_number)
# Тест для получения заказа по трек-номеру
def test_get_order_number():
    response = post_create_order(data.order_body)
    track_number = response.json()["track"]
    get_order = get_order_number(track_number)
    # Проверка, что код ответа равен 200
    assert get_order.status_code == 200