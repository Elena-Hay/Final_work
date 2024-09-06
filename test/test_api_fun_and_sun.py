import allure
import pytest
from pages.API_class import TourApi
from constants import apiURL


api = TourApi(apiURL)


@allure.feature("Заявка для подбора тура менеджером")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("api.Тест проверяет заполнение поля Имя валидными данными")
@allure.severity("critical")
@pytest.mark.parametrize('name',
                         ["Тест",
                          "тест",
                          "ТЕСТ",
                          "Тест Тест"])
def test_positive_fill_name_tour(name):
    email = "Тест@dhd.fh"
    feedback = "callback"
    comments = ""
    result = api.send_request(name, email, feedback, comments)
    with allure.step("Проверить, что заявка успешно отправлена"):
        assert result == 200

@allure.feature("Заявка для подбора тура менеджером")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("api.Тест проверяет заполнение поля Email валидными данными")
@allure.severity("critical")
@pytest.mark.parametrize('email',
                         ["TEST@good.ty",
                          "test-test@good.ty",
                          "test.test@good.ty"])
def test_positive_fill_email_tour(email):
    name = "Тест"
    feedback = "callback"
    comments = ""
    result = api.send_request(name, email, feedback, comments)
    with allure.step("Проверить, что заявка успешно отправлена"):
        assert result == 200

@allure.feature("Заявка для подбора тура менеджером")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("api.Тест проверяет отправку заявки с заполненными комментариями")
@allure.severity("critical")
def test_positive_fill_comments_tour():
    name = "Тест"
    email = "test@hh.ru"
    feedback = "callback"
    comments = "Тестовый тест"
    result = api.send_request(name, email, feedback, comments)
    with allure.step("Проверить, что заявка успешно отправлена"):
        assert result == 200


@allure.feature("Заявка для подбора тура менеджером")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("api.Тест проверяет отправку заявки с разной обратной связью")
@allure.severity("critical")
@pytest.mark.parametrize('feedback',
                         ["callback",
                          "messenger_feedback",
                          "E-mail"])
def test_positive_feedback_tour(feedback):
    name = "Тест"
    email = "test@hh.ru"
    comments = ""
    result = api.send_request(name, email, feedback, comments)
    with allure.step("Проверить, что заявка успешно отправлена"):
        assert result == 200


@allure.feature("Заявка для подбора тура менеджером")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("api.Тест проверяет отправку заявки другим методом")
@allure.severity("critical")
def test_negative_method_tour():
    name = "Тест"
    email = "test@hh.ru"
    feedback = "callback"
    comments = ""
    result = api.send_request_other_method(name, email, feedback, comments)
    with allure.step("Проверить, что заявку не удалось отправить"):
        assert result == 405
