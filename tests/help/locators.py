from selenium.webdriver.common.by import By
# Локаторы

# https://stellarburgers.nomoreparties.site/
# Кнопка Конструктор
button_designer = (By.XPATH, '//*[contains(text(),"Конструктор")]')
# Ссылка/Кнопка «Личный кабинет»
button_profile = (By.XPATH, '//a[@href="/account"]')
# Вкладка "Булки"
tab_bun = (By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Булки")]')
# Выбранная Вкладка "Булки"
selected_bun = (By.XPATH, '//*[contains(@class,"tab_tab_type_current") and contains(.,"Булки")]')
# Вкладка "Соусы"
tab_sauce = (By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Соусы")]')
# Выбранная Вкладка "Соусы"
selected_sauce = (By.XPATH, '//*[contains(@class,"tab_tab_type_current") and contains(.,"Соусы")]')
# Вкладка "Начинки"
tab_topping = (By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Начинки")]')
# Выбранная Вкладка "Начинки"
selected_topping =  (By.XPATH, '//*[contains(@class,"tab_tab_type_current") and contains(.,"Начинки")]')
# Кнопка «Войти в аккаунт»
button_login_account = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')
# Кнопка «Оформить заказ»
button_place_order = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
# https://stellarburgers.nomoreparties.site/register
# Поле Имя
field_name = (By.XPATH,'//*[contains(text(),"Имя")]/parent::*/input')
# Кнопка Зарегистрироваться
button_registration = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')
# Текст ошибки поля Пароль
text_error_password = (By.XPATH, '//*[contains(text(),"Пароль")]/ancestor::div[contains(@class,"input__container")]//p[contains(@class, "input__error")]')
# https://stellarburgers.nomoreparties.site/login
# Кнопка Войти
button_login = (By.XPATH, '//button[contains(text(),"Войти")]')
# Логотип Stellar Burgers
site_logo = (By.XPATH, '//*[contains(@class,"AppHeader_header__logo")]')
# https://stellarburgers.nomoreparties.site/register
# https://stellarburgers.nomoreparties.site/login
# Поле Email
field_email = (By.XPATH, '//*[contains(text(),"Email")]/parent::*/input')
# Поле Пароль
field_password = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')

# https://stellarburgers.nomoreparties.site/forgot-password
# Ссылка на Вход
link_login_page = (By.XPATH, '//a[@href="/login"]')


# https://stellarburgers.nomoreparties.site/account
# Кнопка Выход
button_logout = (By.XPATH, '//button[text()="Выход"]')
# Форма редактирования профиля
form_profile = (By.XPATH, '//*[contains(@class, "Profile_profileList_")]')