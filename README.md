# Проект автотестов для Stellar Burgers

Этот проект содержит набор автотестов для проверки функциональности сайта Stellar Burgers.

---

## **Функциональность, покрытая тестами**

1. **Регистрация:**
   - Генерация случайного Email пользователя. (generate_random_email)
   - Успешная регистрация. (test_successful_registration)
   - Ошибка при некорректном пароле. (test_password_error)

2. **Вход в аккаунт:**
   - Вход через кнопку «Войти в аккаунт» на главной странице. (test_login_via_main_page_button)
   - Вход через кнопку «Личный кабинет». (test_login_via_personal_account_button)
   - Вход через кнопку в форме регистрации. (test_login_via_registration_form_button)
   - Вход через кнопку в форме восстановления пароля. (test_login_via_password_recovery_form_button)

3. **Личный кабинет:**
   - Переход в личный кабинет. (test_go_to_personal_account)
   - Выход из аккаунта. (test_logout)
   - Переход из личного кабинета в конструктор через кнопку «Конструктор». (test_navigate_to_constructor_via_button)
   - Переход из личного кабинета в конструктор через логотип Stellar Burgers. (test_navigate_to_constructor_via_logo)

4. **Конструктор:**
   - Переход к разделам:
     - «Булки» (test_navigate_to_buns_section)
     - «Соусы» (test_navigate_to_sauces_section)
     - «Начинки» (test_navigate_to_fillings_section)
   
5. **Фикстуры для инициализации драйвера и Логина**
   - Открывает и закрывает браузер driver
   - Заполнение полей входа login
