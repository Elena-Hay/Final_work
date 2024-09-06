from selenium.webdriver.common.by import By
import allure
from constants import URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get(URL)

    @allure.step("Заполнить поле Откуда")
    def fill_departure_city(self, city: str) -> None:
        """
        Эта функция принимает на вход город и вводит его в поле Откуда
        """
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[placeholder="Город"]').send_keys(city)

    @allure.step("Подождать заполнения поля Откуда по умолчанию")
    def wait_departure_city(self) -> None:
        """
        Эта функция ждет заполнения поля Откуда по умолчанию
        """
        waiter = WebDriverWait(self.driver, 20)
        waiter.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'input[placeholder="Город"]')))

    @allure.step("Очистить поле Откуда")
    def delete_departure_city(self) -> None:
        """
        Эта функция очищает поле Откуда
        """
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[placeholder="Город"]').clear()

    @allure.step("Получить текст поля Откуда, сообщающий об ошибке")
    def city_no(self) -> str:
        """
        Эта функция возвращает текст ошибки поля Откуда
        """
        waiter = WebDriverWait(self.driver, 20)
        waiter.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, 'div.v-departure__elem'), "Нет совпадений"))
        txt = self.driver.find_element(
            By.CSS_SELECTOR, 'div.v-departure__elem').text
        return txt

    @allure.step("Подождать окно с предложением подключения уведомлений и отказаться")
    def wait_form(self, time: int) -> None:
        """
        Эта функция принимает на вход время, в течение которого ожидает
        появления окна с предложением подключения уведомлений и нажимает 
        на кнопку с отказом от подключения
        """
        waiter = WebDriverWait(self.driver, time)
        if waiter.until(EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, '.popmechanic-title'), 'Будьте в курсе!')):
            self.driver.find_element(
                By.CSS_SELECTOR, 'button.popmechanic-btn.popmechanic-btn-second').click()
        else:
            not waiter
