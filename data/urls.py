class BaseUrls:
    BASE_URL = "http://qa-scooter.praktikum-services.ru"


class CourierUrls:
    CREATE_COURIER = f"{BaseUrls.BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BaseUrls.BASE_URL}/api/v1/courier/login"
    DELETE_COURIER = f"{BaseUrls.BASE_URL}/api/v1/courier/{{courier_id}}"


class OrderUrls:
    CREATE_ORDER = f"{BaseUrls.BASE_URL}/api/v1/orders"
    GET_ORDERS = f"{BaseUrls.BASE_URL}/api/v1/orders"
