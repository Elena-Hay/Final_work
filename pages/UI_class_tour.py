from selenium.webdriver.common.by import By
import allure
from constants import URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tour:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get(URL)

    @allure.step("Перейти в меню Подобрать тур")
    def open_form(self) -> None:
        """
        Эта функция открывает окно с формой для заполнения для подбора тура менеджером
        """
        self.driver.find_element(
            By.CSS_SELECTOR, 'a.v-expert.trslt').click()
        waiter = WebDriverWait(self.driver, 20)
        waiter.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, '.tour-order-popup__header-text'), 'Оставьте заявку и мы подберём вам тур'))

    @allure.step("Заполнить поле Имя")
    def fill_name(self, name: str) -> None:
        """
        Эта функция принимает на вход имя и вводит его в поле Ваше имя
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.name__field.form__field').send_keys(name)

    @allure.step("Заполнить поле Email")
    def fill_mail(self, mail: str) -> None:
        """
        Эта функция принимает на вход e-mail и вводит его в поле Email
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '#login').send_keys(mail)

    @allure.step("Заполнить поле Телефон")
    def fill_phone(self, phone: str) -> None:
        """
        Эта функция принимает на вход телефон и вводит его в поле Телефон
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.ui-telephone__input-min-width').send_keys(phone)

    @allure.step("Подождать появление кнопки Запросить онлайн")
    def wait_button(self, time: int) -> None:
        """
        Эта функция принимает на вход время, в течение которого ожидает
        появления кнопки Запросить онлайн
        """
        waiter = WebDriverWait(self.driver, time)
        waiter.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.tour-order-popup__button')))

    @allure.step("Нажать кнопку Запросить онлайн")
    def button(self) -> None:
        """
        Эта функция отправляет заполненную завку для подбора тура менеджером
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.tour-order-popup__button.notDisabled').click()

    @allure.step("Подождать появление окна с подтверждением заявки")
    def wait(self, time: int) -> None:
        """
        Эта функция принимает на вход время, в течение которого ожидает
        появления подтверждения об отправке заявки
        """
        waiter = WebDriverWait(self.driver, time)
        waiter.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, '.tour-order-title'), 'Заявка успешно отправлена'))

    @allure.step("Нажать на кнопку Отлично")
    def button_ok(self) -> None:
        """
        Эта функция нажимает на кнопку Отлично, после чего окно с уведомлением
        закрывается
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.tour-order-popup__button.default').click()

    @allure.step("Получить текст, сообщающий об успешной отправке заявки")
    def send_success(self) -> str:
        """
        Эта функция возвращает текст об успешной отправке
        """
        txt = self.driver.find_element(
            By.CSS_SELECTOR, '.tour-order-title').text
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
    def get_error(self) -> str:
        """
        Эта функция возвращает текст: "Некорректный адрес электронной почты"
        """
        txt = self.driver.find_element(
            By.CSS_SELECTOR, '.form__field-error').text
        return txt
