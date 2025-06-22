from selenium.webdriver.common.by import By
class Locators:

    # -- Функционал Регистрация --
    ############################################################################
    # Поле регистрации "Имя"
    registration_name = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")

    # Поле регистрации "Email"
    registration_email = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")

    #Поле регистрации "Пароль"
    registration_password = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")

    #Сообщение "Некорректный пароль"
    no_correct_password = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

    # Кнопка Зарегистрироваться на форме Вход
    button_registration_entrance = (By.XPATH, '//a[text()="Зарегистрироваться"]')

    # Кнопка Зарегистрироваться на форме Вход
    button_registration_register = (By.XPATH, '//button[text()="Зарегистрироваться"]')


    # -- Функционал Вход --
    ###########################################################################
    # Кнопка "Войти в аккаунт" на главной
    button_entrance_account = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # Кнопка "Войти" в форме Вход
    button_entrance_in_login_page = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Поле "Email" в окне "Вход"
    field_email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле "Пароль" в окне "Вход"
    field_password = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

    # Кнопка "Оформить заказ"
    place_order = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Кнопка "Войти" в форме регистрации
    link_entrance_registration = (By.XPATH, '//a[text()="Войти"]')

    # Ссылка "Восстановить пароль"
    link_recovery_password = (By.XPATH, "//a[text()='Восстановить пароль']")

    # Кнопка "Войти" в форме восстановления пароля
    link_entrance_forget_password = (By.XPATH, '//a[text()="Войти"]')

    # Заголовок Вход на странице входа
    text_entrance = (By.XPATH, '//h2[text()="Вход"]')

    # Кнопка "Войти" в Личном кабинете
    button_entrance_private_area = (By.XPATH, "//button[contains(text(), 'Войти')]")


    # -- Функционал Личного Кабинета --
    ##############################################################################
    # Кнопка "Личный кабинет"
    button_private_area = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Текст "Профиль" в Личном кабинете
    link_profile = (By.XPATH, '//a[text()="Профиль"]')

    # Логотип Stellar Burgers
    logotype = (By.XPATH, '//header/nav/div')

    # Кнопка "Выйти" в Личном кабинете
    button_exit = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Заголовок "Соберите бургер"
    create_burger = (By.XPATH, '//h1[text()="Соберите бургер"]')


    # -- Функционал Конструктора
    ################################################################################
    # Линк "Конструктор"
    link_construction = (By.XPATH, '//p[text()="Конструктор"]')

    # Линк "Булки"
    inscription_bread = (By.XPATH, '//span[text() = "Булки"]')

    # Заголовок "Булки"
    header_bread = (By.XPATH, '//h2[text() = "Булки"]')

    # Линк "Соусы"
    inscription_souse = (By.XPATH, '//span[text() = "Соусы"]')

    # Заголовок "Соусы"
    header_souse = (By.XPATH, '//h2[text() = "Соусы"]')

    # Линк "Начинки"
    inscription_filling = (By.XPATH, '//span[text() = "Начинки"]')

    # Заголовок "Начинки"
    header_filling = (By.XPATH, '//h2[text() = "Начинки"]')

    # Активный элемент Конструктора
    active_element_constructor = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect")]')




