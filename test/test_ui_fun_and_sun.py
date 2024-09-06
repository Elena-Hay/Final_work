from selenium import webdriver
import pytest
import allure
from pages.UI_class_tour import Tour
from pages.UI_class_search import Search
from pages.UI_class_authtorization import Authtorization
from constants import email


@allure.feature("Заявка для подбора тура менеджером")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("Тест проверяет заполнение поля Email валидными данными")
@allure.severity("critical")
@pytest.mark.parametrize('mail',
                         ["TEST@good.ty",
                          "test-test@good.ty",
                          "test.test@good.ty"])
def test_positive_fill_mail(mail):
    browser = webdriver.Chrome()
    tour = Tour(browser)
    tour.open()
    tour.wait_window(20)
    tour.open_form()
    tour.fill_name("Тест")
    tour.fill_mail(mail)
    tour.fill_phone("123-456-78-90")
    tour.wait_button(20)
    tour.button()
    tour.wait(20)
    result = tour.send_success()
    tour.button_ok()
    with allure.step("Проверить, что заявка успешно отправлена"):
        assert result == "Заявка успешно отправлена"
    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.feature("Заявка для подбора тура менеджером")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("Тест проверяет заполнение поля Email невалидными данными")
@allure.severity("critical")
@pytest.mark.parametrize('mail',
                         ["good.ty",
                          "!!!!!!;",
                          "test@goodty"])
def test_negative_fill_mail(mail):
    browser = webdriver.Chrome()
    tour = Tour(browser)
    tour.open()
    tour.wait_window(20)
    tour.open_form()
    tour.fill_name("Тест")
    tour.fill_mail(mail)
    tour.fill_phone("123-456-78-90")
    result = tour.get_error()
    with allure.step("Проверить, что поле не принимает введенное значение"):
        assert result == "Некорректный адрес электронной почты"
    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.feature("Авторизация")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("Тест проверяет возможность авторизоваться")
@allure.severity("critical")
def test_positive_authtorization():
    browser = webdriver.Chrome()
    auth = Authtorization(browser)
    auth.open()
    auth.wait_window(20)
    auth.open_form()
    auth.fill_email(email)
    auth.fill_password()
    auth.wait_button(20)
    auth.open_wait()
    result = auth.get_mail()

    with allure.step("Проверить, что пользователь успешно вошел в аккаунт"):
        assert result == email
    with allure.step("Закрыть браузер"):
        browser.quit()

@allure.feature("Авторизация")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("Тест проверяет заполнение поля Email при авторизации невалидными данными")
@allure.severity("critical")
@pytest.mark.parametrize('mail',
                         ["good.ty",
                          "!!!!!!;",
                          "test@goodty"])
def test_negative_authtorization_email(mail):
    browser = webdriver.Chrome()
    auth = Authtorization(browser)
    auth.open()
    auth.wait_window(20)
    auth.open_form()
    auth.fill_email(mail)
    auth.fill_password()
    result = auth.get_mail_error()

    with allure.step("Проверить, что поле не принимает введенное значение"):
        assert result == "Некорректный адрес электронной почты"
    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.feature("Поиск тура")
@allure.title("Туристическая компания FUN&SUN")
@allure.description("Тест проверяет заполнение поля Откуда невалидными значениями")
@allure.severity("blocker")
@pytest.mark.parametrize('city',
                         ["dhdshd",
                          "всвсв"])
def test_negative_search_departure_city(city):
    browser = webdriver.Chrome()
    search = Search(browser)
    search.open()
    search.wait_form(60)
    search.wait_departure_city()
    search.delete_departure_city()
    search.fill_departure_city(city)
    result = search.city_no()

    with allure.step("Проверить, что поле не принимает невалидные данные"):
        assert result == "Нет совпадений"
    with allure.step("Закрыть браузер"):
        browser.quit()
