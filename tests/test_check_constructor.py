# Проверка функциональности раздела «Конструктор»

from locators import Locators
from tests.conftest import driver


class TestCheckConstructor: # проверяем переход на раздел Соусы
    def test_check_crossing_souse(self, driver):
        driver.find_element(*Locators.link_construction).click() # переходим в конструктор
        driver.find_element(*Locators.inscription_souse).click() # выбираем Соусы

        assert driver.find_element(*Locators.inscription_souse).is_displayed() and driver.find_element(*Locators.active_element_constructor).text == "Соусы"

    def test_check_crossing_filling(self, driver): # проверяем переход на раздел Начинки
        driver.find_element(*Locators.link_construction).click()  # переходим в конструктор
        driver.find_element(*Locators.inscription_filling).click()  # выбираем Начинки

        assert driver.find_element(*Locators.inscription_filling).is_displayed() and driver.find_element(*Locators.active_element_constructor).text == "Начинки"

    def test_check_crossing_bread(self, driver): # проверяем переход на раздел Булки
        driver.find_element(*Locators.link_construction).click()  # переходим в конструктор
        driver.find_element(*Locators.inscription_filling).click()  # выбираем Начинки
        driver.find_element(*Locators.inscription_bread).click()  # выбираем Булки

        assert driver.find_element(*Locators.inscription_bread).is_displayed() and driver.find_element(*Locators.active_element_constructor).text == "Булки"