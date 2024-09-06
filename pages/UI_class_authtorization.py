from selenium.webdriver.common.by import By
import allure
from constants import URL
from constants import password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Authtorization:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get(URL)

    @allure.step("Перейти в меню Войти")
    def open_form(self) -> None:
        """
        Эта функция открывает окно с формой для входа в аккаунт
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.v-icon-user-14').click()
        waiter = WebDriverWait(self.driver, 20)
        waiter.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, 'h4.h4'), 'Войти или зарегистрироваться'))

    @allure.step("Заполнить поле Email")
    def fill_email(self, email) -> None:
        """
        Эта функция принимает на вход email и вводит его в поле Email
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '#email').send_keys(email)

    @allure.step("Заполнить поле пароль")
    def fill_password(self) -> None:
        """
        Эта функция принимает на вход пароль и вводит его в поле Пароль
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys(password)

    @allure.step("Подождать появление кнопки Войти и нажать")
    def wait_button(self, time: int) -> None:
        """
        Эта функция принимает на вход время, в течение которого ожидает
        появления кнопки Войти и нажимает на нее
        """
        waiter = WebDriverWait(self.driver, time)
        waiter.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.new-button.new-button__primary'))).click()

    @allure.step("Войти в профиль")
    def open_wait(self) -> None:
        """
        Эта функция входит в профиль
        """
        waiter = WebDriverWait(self.driver, 20)
        waiter.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'img.v-account-img')))
        waiter.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'img.v-account-img'))).click()
        self.driver.find_element(
            By.CSS_SELECTOR, 'span.user-menu-link.body_s').click()

    @allure.step("Найти Email, под которым вошли в аккаунт")
    def get_mail(self) -> str:
        """
        Эта функция возвращает текст с email пользователя, с которым авторизовались
        """
        waiter = WebDriverWait(self.driver, 20)
        txt = waiter.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'p.user-data-email.body_s_s'))).text
        return txt

    @allure.step("Подождать окно с предложением подключения уведомлений")
    def wait_window(self, time: int) -> None:
        """
        Эта функция принимает на вход время, в течение которого ожидает
        появления окна с предложением подключения уведомлений
        """
        waiter = WebDriverWait(self.driver, time)
        if waiter.until(EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, '.popmechanic-title'), 'Будьте в курсе!')):
            self.driver.find_element(
                By.CSS_SELECTOR, 'button.popmechanic-btn.popmechanic-btn-second').click()
        else:
            not waiter

    @allure.step("Получить текст, сообщающий об ошибке заполнения поля Email")
    def get_mail_error(self) -> str:
        """
        Эта функция возвращает текст: "Некорректный адрес электронной почты"
        """
        waiter = WebDriverWait(self.driver, 20)
        txt = waiter.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.form__field-error.popup__text-error'))).text
        return txt
