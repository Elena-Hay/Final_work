import allure
import requests
from constants import token
from constants import cookie


class TourApi:
    def __init__(self, url: str) -> None:
        self.url = url

    @allure.step("api. Отправить заявку по подбору тура менеджером")
    def send_request(self, name: str, email: str, feedback: str, comments: str) -> int:
        """
        Эта функция принимает на вход параметры: имя, почту, обратную связь, комментарии, 
        отправляет заявку менеджеру, возвращает статус-код в виде числа.
        """
        form = {
            "name": name,
            "phone": "71111111111",
            "email": email,
            "feedback": feedback,
            "comments": comments,
            "businessUnitFromSiteUrl": None,
            "ga": "GA1.2.2141310459.1716372340"
        }
        my_headers = {}
        my_headers["Cookie"] = 'XSRF-TOKEN=' + token + cookie
        my_headers["Content-Type"] = 'application/json'
        my_headers["x-xsrf-token"] = token
        resp = requests.post(self.url, json=form, headers=my_headers)
        return resp.status_code

    @allure.step("api. Отправить заявку по подбору тура менеджером другим методом")
    def send_request_other_method(self, name: str, email: str, feedback: str, comments: str) -> int:
        """
        Эта функция принимает на вход параметры: имя, почту, обратную связь, комментарии, 
        отправляет заявку менеджеру, возвращает статус-код в виде числа.
        """
        form = {
            "name": name,
            "phone": "71111111111",
            "email": email,
            "feedback": feedback,
            "comments": comments,
            "businessUnitFromSiteUrl": None,
            "ga": "GA1.2.2141310459.1716372340"
        }
        my_headers = {}
        my_headers["Cookie"] = 'XSRF-TOKEN=' + token + cookie
        my_headers["Content-Type"] = 'application/json'
        my_headers["x-xsrf-token"] = token
        resp = requests.put(self.url, json=form, headers=my_headers)
        return resp.status_code
