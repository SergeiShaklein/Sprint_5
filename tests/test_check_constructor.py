# Проверка функциональности раздела «Конструктор»
import pytest
from locators import Locators
from tests.conftest import driver


@pytest.mark.parametrize("section, inscription", [
    (Locators.inscription_souse, "Соусы"),
    (Locators.inscription_filling, "Начинки"),
    (Locators.inscription_bread, "Булки"),
])
class TestCheckConstructor:
    def test_check_crossing_sections(self, driver, section, inscription):
        driver.find_element(*Locators.link_construction).click()  # переходим в конструктор

        if section == Locators.inscription_bread:
            driver.find_element(*Locators.inscription_souse).click()  # выбираем Соусы перед Булками

        driver.find_element(*section).click()  # выбираем нужный раздел

        assert driver.find_element(*section).is_displayed() and driver.find_element(
            *Locators.active_element_constructor).text == inscription