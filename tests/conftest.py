# Фикстуры на часто используемые дейстивия
# 1) Вход на страницу регистрации, используем чтобы
# - проверить пустое поле Имя
# - проверить сообщение Некорректный пароль
# - зарегестрироваться (используем в каждом тесте)
# 2) Вход на страницу Авторизации используем для
# - проверки ЛК
# - проверки кнопки Вход

import pytest
from selenium import webdriver
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Credantial

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_site) # заходим на главную
    yield driver
    driver.quit()

@pytest.fixture
def registration(driver):

    driver.find_element(*Locators.button_entrance_account).click() # ищем кнопку Войти в аккаунт и кликаем
    driver.find_element(*Locators.button_registration_entrance).click()  # ищем кнопку Зарегестрироваться и кликаем
    return driver

@pytest.fixture
def authorization(driver):

    driver.find_element(*Locators.button_entrance_account).click() # ищем кнопку Войти в аккаунт и кликаем
    driver.find_element(*Locators.field_email).send_keys(Credantial.email) # заполняем поле email
    driver.find_element(*Locators.field_password).send_keys(Credantial.password) # заполняем поле Пароль
    driver.find_element(*Locators.button_entrance_in_login_page).click() # кликаем на Войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.place_order)) # ждем загрузки кнопки Оформить заказ (доступна только после авторизации)
    driver.find_element(*Locators.button_private_area).click()  # кликаем Личный кабинет
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_exit))  # ждем кнопки Выход

    return driver