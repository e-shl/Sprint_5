# qa_python

# Описание проведённых тестов

# Проверь, что работают переходы к разделам
# Проверь переход к разделу «Булки»
test_designer_page.py::test_designer_click_bun_is_opened_bun PASSED      [  5%]
# Проверь переход к разделу «Соусы»
test_designer_page.py::test_designer_click_sauce_is_opened_sauce PASSED  [ 11%]
# Проверь переход к разделу «Начинки»
test_designer_page.py::test_designer_click_topping_is_opened_topping PASSED [ 17%]

# Проверь выход из аккаунта на странице профиля что открывается страница входа
test_exit_profile_page.py::test_exit_profile_is_open_login_page PASSED   [ 23%]

# Проверь переход по клику на «Личный кабинет».
test_link_profile_page.py::test_link_profile_is_opened_profile_page PASSED [ 29%]

# Проверь Вход
# Проверь удачный вход по кнопке «Войти в аккаунт» на главной
test_login_page.py::test_authorization_from_home_is_successful_authorization PASSED [ 35%]
# Проверь удачный вход через кнопку «Личный кабинет»
test_login_page.py::test_authorization_from_button_profile_is_successful_authorization PASSED [ 41%]
# Проверь удачный вход через кнопку в форме регистрации
test_login_page.py::test_authorization_from_register_is_successful_authorization PASSED [ 47%]
# Проверь удачный вход через кнопку в форме восстановления пароля
test_login_page.py::test_authorization_from_forgot_password_is_successful_authorization PASSED [ 52%]

# Проверить удачную регистрацию
test_register_page.py::test_registration_is_successful_registration[123456] PASSED [ 58%]
test_register_page.py::test_registration_is_successful_registration[1234567] PASSED [ 64%]
test_register_page.py::test_registration_is_successful_registration[1234567891] PASSED [ 70%]
# Проверить ошибку для пароля меньше 6 символов
test_register_page.py::test_registration_less6_password_is_error_message[1] PASSED [ 76%]
test_register_page.py::test_registration_less6_password_is_error_message[1234] PASSED [ 82%]
test_register_page.py::test_registration_less6_password_is_error_message[12345] PASSED [ 88%]

# Проверь переход в конструктор по клику на «Конструктор»
test_transition_designer_page.py::test_click_logo_is_opened_designer_page PASSED [ 94%]
# Проверь переход в конструктор по клику на логотип Stellar Burgers
test_transition_designer_page.py::test_click_designer_button_is_opened_designer_page PASSED [100%]
