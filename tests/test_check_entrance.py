# Проверки функциональности кнопок "Вход":

import pytest
from locators import Locators
from curl import *
from data import Credantial
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# вход по кнопке «Войти в аккаунт» на главной
class TestCheckButtonEntranceInAccount:
    def test_entrance_button_in_main_page(self, driver):
        driver.find_element(*Locators.button_entrance_account).click()

        assert driver.current_url == login_site  # проверяем, что мы на странице Вход

# вход через кнопку «Личный кабинет»
class TestCheckButtonEntranceInPrivateArea:
    def test_entrance_button_in_private_page(self, driver):
        driver.find_element(*Locators.button_private_area).click()  # кликаем Личный кабинет, переходим на форму входа
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)  # заполняем поле email
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)  # заполняем поле пароль
        driver.find_element(*Locators.button_entrance_in_login_page).click() # жмем Вход
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.place_order))  # ждем загрузки кнопки Оформить заказ (доступна только после авторизации)
        driver.find_element(*Locators.button_private_area).click()  # кликаем Личный кабинет
        assert driver.current_url == account_site  # проверяем, что вошли и авторизовались

# вход через кнопку в форме регистрации
@pytest.mark.usefixtures("registration")
class TestCheckButtonEntranceInRegistration:
    def test_entrance_button_in_registration(self, driver):
        driver.find_element(*Locators.link_entrance_registration).click()

        assert driver.current_url == login_site  # проверяем, что мы на странице Вход

# вход через кнопку в форме восстановления пароля
class TestCheckButtonEntranceInRecovery:
    def test_entrance_button_in_recovery_page(self, driver):
        driver.find_element(*Locators.button_entrance_account).click()
        driver.find_element(*Locators.link_recovery_password).click()
        driver.find_element(*Locators.link_entrance_forget_password).click()

        assert driver.current_url == login_site  # проверяем, что мы на странице Вход
