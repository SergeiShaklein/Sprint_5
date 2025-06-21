# Проверки функциональности Личного Кабинета:

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *

# Проверка перехода по клику на «Личный кабинет».
@pytest.mark.usefixtures("authorization")
class TestCheckMoveToAccount:
    def test_check_logout(self, driver):

        assert driver.current_url == profile_site # проверяем, что мы в личном кабинете

# Проверка выхода по кнопке «Выйти» в личном кабинете.
@pytest.mark.usefixtures("authorization")
class TestCheckButtonExitFromAccount:
    def test_check_logout(self, driver):
        driver.find_element(*Locators.button_exit).click() # кликаем Выход
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.text_entrance)) # ждем заголовок формы Вход

        assert driver.current_url == login_site # проверяем, что мы деавторизовались и на странице Вход

# Проверка перехода по клику на «Конструктор»
@pytest.mark.usefixtures("authorization")
class TestMoveToConstructor:
    def test_move_constructor(self, driver):
        driver.find_element(*Locators.link_construction).click() # кликаем Конструктор
        create_burger_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.create_burger)).text  # ждем загрузки Конструктора

        assert create_burger_text == 'Соберите бургер' # проверяем, что видим конструктор


# Проверка перехода по клику на логотип Stellar Burgers.
@pytest.mark.usefixtures("authorization")
class TestMoveLogo:
    def test_move_constructor(self, driver):
        driver.find_element(*Locators.logotype).click() # кликаем на лого
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.create_burger))  # ждем загрузки Конструктора

        assert driver.current_url == main_site # проверяем, что на главной