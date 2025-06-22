# Проверка функциональности Регистрации:

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from generator_lp import GenerationEmailPassword
import random
import string

# Успешная регистрация.
@pytest.mark.usefixtures("registration")
class TestNewCorrectRegistration:
    def test_correct_registration(self, driver):
        generator = GenerationEmailPassword()
        generate_name, generate_email, generate_password = generator.generate_login()
        driver.find_element(*Locators.registration_name).send_keys(generate_name)  # генерируем имя
        driver.find_element(*Locators.registration_email).send_keys(generate_email)  # генерируем email
        driver.find_element(*Locators.registration_password).send_keys(generate_password)  # генерируем пароль
        driver.find_element(*Locators.button_registration_register).click() # регистрируемся
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_entrance_in_login_page)) # ждем загрузки формы Входа
        driver.find_element(*Locators.field_email).send_keys(generate_email)  # заполняем поле email
        driver.find_element(*Locators.field_password).send_keys(generate_password)  # заполняем поле пароль
        driver.find_element(*Locators.button_entrance_in_login_page).click()  # кликаем на Войти
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.place_order))  # ждем загрузки кнопки Оформить заказ (доступна только после авторизации)
        driver.find_element(*Locators.button_private_area).click()  # кликаем Личный кабинет
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_exit))  # ждем кнопки Выход

        assert driver.current_url == profile_site # проверяем что у нас появился свой личный кабинет

# Поле «Имя» не должно быть пустым, проверяем что регистрация не проходит
@pytest.mark.usefixtures("registration")
class TestNonameRegistration:
    def test_noname_registration(self, driver):
        generator = GenerationEmailPassword()
        generate_name, generate_email, generate_password = generator.generate_login()
        driver.find_element(*Locators.registration_name).send_keys('')  # поле имя оставляем пустым
        driver.find_element(*Locators.registration_email).send_keys(generate_email)  # генерируем email
        driver.find_element(*Locators.registration_password).send_keys(generate_password)  # генерируем пароль
        driver.find_element(*Locators.button_registration_register).click() # пытаемся зарегистрироваться

        assert driver.current_url == register_site  # проверяем что мы все еще на форме регистрации

# Проверяем, что если пароль менее шести символов, появляется Ошибка для некорректного пароля
@pytest.mark.usefixtures("registration")
class TestShortPassword:
    def test_short_password_registration(self, driver):
        generator = GenerationEmailPassword()
        generate_name, generate_email, _ = generator.generate_login()
        password_length = random.randint(1, 5)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        short_password = f"{random_string}"
        driver.find_element(*Locators.registration_name).send_keys(generate_name)  # вставляем имя
        driver.find_element(*Locators.registration_email).send_keys(generate_email)  # вставляем email
        driver.find_element(*Locators.registration_password).send_keys(short_password)  # вставляем короткий пароль
        driver.find_element(*Locators.button_registration_register).click()  # пытаемся зарегистрироваться
        error_text =  driver.find_element(*Locators.no_correct_password).text

        assert error_text == "Некорректный пароль"
