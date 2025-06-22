# Проверки функциональности Личного Кабинета:

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from data import Credantial

# Проверка перехода по клику на «Личный кабинет».
class TestCheckClickAccount:
    def test_move_to_account(self, driver):
        driver.find_element(*Locators.button_private_area).click()  # кликаем Личный кабинет
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)  # заполняем поле email
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)  # заполняем поле Пароль
        driver.find_element(*Locators.button_entrance_in_login_page).click()  # кликаем на Войти
        driver.find_element(*Locators.button_private_area).click()  # кликаем Личный кабинет
        assert driver.current_url == account_site # проверяем, что мы в личном кабинете

@pytest.mark.usefixtures("authorization")
class TestCheckMoveFromAccount:
# Проверка выхода по кнопке «Выйти» в личном кабинете.
    def test_check_logout(self, driver):
        driver.find_element(*Locators.button_exit).click() # кликаем Выход
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.text_entrance)) # ждем заголовок формы Вход

        assert driver.current_url == login_site # проверяем, что мы деавторизовались и на странице Вход

# Проверка перехода по клику на «Конструктор»
    def test_move_constructor(self, driver):
        driver.find_element(*Locators.link_construction).click() # кликаем Конструктор
        create_burger_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.create_burger)).text  # ждем загрузки Конструктора

        assert create_burger_text == 'Соберите бургер' # проверяем, что видим конструктор


# Проверка перехода по клику на логотип Stellar Burgers.
    def test_move_by_logo(self, driver):
        driver.find_element(*Locators.logotype).click() # кликаем на лого
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.create_burger))  # ждем загрузки Конструктора

        assert driver.current_url == main_site # проверяем, что на главной