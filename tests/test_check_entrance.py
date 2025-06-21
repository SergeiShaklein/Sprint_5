# Проверки функциональности кнопок "Вход":

import pytest
from locators import Locators
from curl import *


# вход по кнопке «Войти в аккаунт» на главной
class TestCheckButtonEntranceInAccount:
    def test_entrance_button_in_main_page(self, driver):
        driver.find_element(*Locators.button_entrance_account).click()

        assert driver.current_url == login_site  # проверяем, что мы на странице Вход

# вход через кнопку «Личный кабинет»
@pytest.mark.usefixtures("authorization")
class TestCheckButtonEntranceInPrivateArea:
    def test_entrance_button_in_main_page(self, driver):

        assert driver.current_url == profile_site  # проверяем, что вошли и авторизовались

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
