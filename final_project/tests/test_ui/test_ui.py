from random import randint
import pytest
from base_ui import BaseCase
import requests
import allure


class TestLoginForm(BaseCase):
    @pytest.mark.parametrize(
        'username, password',
        [pytest.param('', 'passwordvalid'), pytest.param('loginvalid', ''), pytest.param('', '')]
                            )
    @pytest.mark.UI
    @allure.feature('Form of authorization')
    def test_negative_empty_fields(self, username, password):
        """Проверка входа с пустым полями:
           1. username
           2. password
           3. username и password
           Ожидаемый результат - остаемся на странице авторизации."""
        with allure.step('Логинемся с невалидным логином или паролем'):
            self.login_page.login(username, password)
        self.base_page.screenshot("screen_1")
        with allure.step('Пытаемся найти локатор ввода имени пользователя'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.login_page.locators.USERNAME_FIELD)

    @pytest.mark.parametrize(
        'username',
        [pytest.param('1' * 3), pytest.param('1' * 17)]
                            )
    @pytest.mark.UI
    @allure.feature('Form of authorization')
    def test_negative_incorrect_username_length(self, username):
        """Проверка граничных значений поля username (корректная длина поля - [6;16]).
           Ожидаемый результат - всплывающее сообщение 'Incorrect username length'."""
        with allure.step('Генерируем валидный пароль'):
            password = self.builder.password()
        with allure.step('Логинемся с невалидным логином'):
            self.login_page.login(username, password)
        with allure.step('Пытаемся найти локатор с ошибкой Incorrect username length'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.login_page.locators.INCORRECT_USERNAME_LENGTH)

    @pytest.mark.UI
    @allure.feature('Form of authorization')
    def test_negative_login_unregistered_user(self):
        """Проверка входа незарегестрированного пользователя.
           Ожидаемый результат - всплывающее сообщение 'Invalid username or password'."""
        with allure.step('Генерируем валидный логин и пароль'):
            login = self.builder.login()
            password = self.builder.password()
        with allure.step('Логинемся с незарегестрированным логином и паролем'):
            self.login_page.login(login, password)
        with allure.step('Пытаемся найти локатор с ошибкой Invalid username or password'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.login_page.locators.INVALID_USERNAME_OR_PASSWORD)

    @pytest.mark.UI
    @allure.feature('Form of authorization')
    def test_auth_registered_user(self, new_user):
        """Проверка входа зарегестрированного пользователя.
           Ожидаемый результат - появление домашней страницы."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            login = new_user.username
            password = new_user.password
        with allure.step('Логинемся с зарегестрированным логином и паролем'):
            self.base_page.screenshot("screen_1")
            self.login_page.login(login, password)
        with allure.step('Пытаемся найти локатор домашней страницы HOME'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.main_page.locators.HOME)

    @pytest.mark.UI
    @allure.feature('Form of authorization')
    def test_auth_registered_user(self, new_user):
        """Проверка входа и выхода зарегестрированного пользователя.
           Ожидаемый результат - появление домашней страницы."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            login = new_user.username
            password = new_user.password
        with allure.step('Логинемся с зарегестрированным логином и паролем и нажимаем logout'):
            self.login_page.logout(login, password)
        with allure.step('Пытаемся найти локатор ввода имени пользователя'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.login_page.locators.USERNAME_FIELD)


class TestRegistrationForm(BaseCase):
    @pytest.mark.parametrize(
        'username',
        [pytest.param('1' * 3), pytest.param('1' * 17)]
                            )
    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_incorrect_username_length(self, username):
        """Проверка граничных значений поля username (корректная длина поля - [6;16]).
           Ожидаемый результат - всплывающее сообщение 'Incorrect username length'."""
        with allure.step('Генерируем валидный email и пароль'):
            email = self.builder.email()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Логинемся с невалидным логином'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с ошибкой Incorrect username length'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.INCORRECT_USERNAME_LENGTH)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_incorrect_password_length(self):
        """Проверка граничных значений поля password (корректная длина поля - [1;255]).
           Ожидаемый результат - всплывающее сообщение 'Incorrect password length'."""
        with allure.step('Генерируем валидный логин и email'):
            username = self.builder.login()
            email = self.builder.email()
        with allure.step('Генерируем невалидный пароль'):
            password = '1' * 256
            confirm_password = password
        with allure.step('Регистрируемся с невалидным паролем'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти сообщение с ошибкой Incorrect username length на странице'):
            self.base_page.screenshot("screen_1")
            assert "Incorrect password length" in self.driver.page_source

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_incorrect_email_length(self):
        """Проверка граничных значений поля email (корректная длина поля - [1;64]).
           Ожидаемый результат - всплывающее сообщение 'Incorrect email length'."""
        with allure.step('Генерируем валидный логин и пароль'):
            username = self.builder.login()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Генерируем невалидный email'):
            email = '1' * 65 + '@mail.ru'
        with allure.step('Регистрируемся с невалидным email'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с ошибкой Incorrect email length'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.INCORRECT_EMAIL_LENGTH)

    @pytest.mark.parametrize(
        'email',
        [pytest.param('invalidemail' + '@mailru'), pytest.param('invalidemail' + 'mail.ru')]
                            )
    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_invalid_email_address(self, email):
        """Проверка регистрации с невалидным email.
           Ожидаемый результат - всплывающее сообщение 'Invalid email address'."""
        with allure.step('Генерируем валидный логин и пароль'):
            username = self.builder.login()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с невалидным email'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с ошибкой Invalid email address'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.INVALID_EMAIL_ADDRESS)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_password_mismatch(self):
        """Проверка регистрации с несовпадением полей password и confirm password.
           Ожидаемый результат - всплывающее сообщение 'Password must match'."""
        with allure.step('Генерируем валидный логин и email'):
            username = self.builder.login()
            email = self.builder.email()
        with allure.step('Генерируем разные пароли'):
            password = self.builder.password()
            confirm_password = self.builder.password()
        with allure.step('Регистрируемся с с разными полями password и confirm password'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с ошибкой Password must match'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.PASSWORDS_MUST_MATCH)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_do_not_accept_SDET(self):
        """Проверка регистрации с отрицательным условием 'I accept that I want to be a SDET'.
           Ожидаемый результат - остаемся на странице регистрации."""
        with allure.step('Генерируем валидный логин, пароль и email'):
            username = self.builder.login()
            email = self.builder.email()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с отрицательным условием "I accept that I want to be a SDET"'):
            self.registration_page.registration(username, email, password, confirm_password, accept=False)
        with allure.step('Пытаемся найти локатор с кнопкой подтверждения регистрации REGISTER'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.REGISTER_SUBMIT)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_existing_login(self, new_user):
        """Проверка регистрации с уже существующим логином.
           Ожидаемый результат - всплывающее сообщение 'User already exists'."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
        with allure.step('Генерируем валидный пароль и email'):
            email = self.builder.email()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с уже существующим логином'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с ошибкой User already exists'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.USER_ALREADY_EXISTS)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_existing_email(self, new_user):
        """Проверка регистрации с уже существующим email.
           Ожидаемый результат - всплывающее сообщение 'User already exists'."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            email = new_user.email
        with allure.step('Генерируем валидный логин и пароль'):
            username = self.builder.login()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с уже существующим email'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти сообщение с ошибкой User already exists на странице'):
            self.base_page.screenshot("screen_1")
            assert "User already exists" in self.driver.page_source

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_reg_existing_user(self, new_user):
        """Проверка регистрации с уже существующего пользователя.
           Ожидаемый результат - всплывающее сообщение 'User already exists'."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            email = new_user.email
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с данными уже сущетсвующего пользователя'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с ошибкой User already exists'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.USER_ALREADY_EXISTS)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_empty_login_field(self):
        """Проверка регистрации с пустым полем username.
           Ожидаемый результат - остаемся на странцие регистрации."""
        with allure.step('Генерируем невалидный логин'):
            username = ''
        with allure.step('Генерируем валидный логин и email'):
            email = self.builder.email()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с невалидным логином'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с кнопкой подтверждения регистрации REGISTER'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.REGISTER_SUBMIT)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_empty_email_field(self):
        """Проверка регистрации с пустым полем email.
           Ожидаемый результат - остаемся на странцие регистрации."""
        with allure.step('Генерируем невалидный email'):
            email = ''
        with allure.step('Генерируем валидный логин и пароль'):
            username = self.builder.login()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с невалидным email'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с кнопкой подтверждения регистрации REGISTER'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.REGISTER_SUBMIT)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_negative_empty_password_field(self):
        """Проверка регистрации с пустым полем password.
           Ожидаемый результат - остаемся на странцие регистрации."""
        with allure.step('Генерируем невалидный пароль'):
            password = ''
            confirm_password = password
        with allure.step('Генерируем валидный логин и email'):
            username = self.builder.login()
            email = self.builder.email()
        with allure.step('Регистрируемся с невалидным паролем'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с кнопкой подтверждения регистрации REGISTER'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.registration_page.locators.REGISTER_SUBMIT)

    @pytest.mark.UI
    @allure.feature('Form of registration')
    def test_valid_registered_user(self):
        """Проверка регистрации успешной регистрации.
           Ожидаемый результат - переходим на домашнюю странцу."""
        with allure.step('Генерируем валидный логин, пароль и email'):
            username = self.builder.login()
            email = self.builder.email()
            password = self.builder.password()
            confirm_password = password
        with allure.step('Регистрируемся с валидными данными'):
            self.registration_page.registration(username, email, password, confirm_password)
        with allure.step('Пытаемся найти локатор с кнопкой возвращения на домашнюю страницу HOME'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_element_presented(self.main_page.locators.HOME)


class TestMainPage(BaseCase):
    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_python(self, auto):
        """Проверка перехода по кнопке Python.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://www.python.org/'."""
        with allure.step('Кликаем по кнопке Python'):
            self.main_page.go_to_python()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://www.python.org/" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_python_history(self, auto):
        """Проверка перехода по кнопке Python history.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://en.wikipedia.org/wiki/History_of_Python'."""
        with allure.step('Кликаем по кнопке Python history'):
            self.main_page.go_to_python_history()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://en.wikipedia.org/wiki/History_of_Python" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_about_flask(self, auto):
        """Проверка перехода по кнопке About Flask.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://flask.palletsprojects.com/en/1.1.x/#'."""
        with allure.step('Кликаем по кнопке About Flask'):
            self.main_page.go_to_about_flask()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://flask.palletsprojects.com/en/1.1.x/#" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_download_centos7(self, auto):
        """Проверка перехода по кнопке Download Centos7.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://www.centos.org/download/'."""
        with allure.step('Кликаем по кнопке Download Centos7'):
            self.main_page.go_to_download_centos7()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://www.centos.org/download/" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_network_wireshark_news(self, auto):
        """Проверка перехода по кнопке Wireshark News.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://www.wireshark.org/news/'."""
        with allure.step('Кликаем по кнопке News'):
            self.main_page.go_to_network_wireshark_news()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://www.wireshark.org/news/" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_network_wireshark_download(self, auto):
        """Проверка перехода по кнопке Wireshark Download.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://www.wireshark.org/#download'."""
        with allure.step('Кликаем по кнопке Download'):
            self.main_page.go_to_network_wireshark_download()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://www.wireshark.org/#download" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_network_tcpdump_examples(self, auto):
        """Проверка перехода по кнопке TCPDUMP Examples.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://hackertarget.com/tcpdump-examples/'."""
        with allure.step('Кликаем по кнопке Examples'):
            self.main_page.go_to_network_tcpdump_examples()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://hackertarget.com/tcpdump-examples/" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_api_wikipedia(self, auto):
        """Проверка перехода по кнопке под надписью 'What is an API?'.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://en.wikipedia.org/wiki/API'."""
        with allure.step('Кликаем по кнопке под надписью "What is an API?"'):
            self.main_page.go_to_api_wikipedia()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://en.wikipedia.org/wiki/API" == self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_future_of_internet(self, auto):
        """Проверка перехода по кнопке под надписью 'Future of internet'.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу
           'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'."""
        with allure.step('Кликаем по кнопке под надписью "Future of internet"'):
            self.main_page.go_to_future_of_internet()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "future-of-the-internet" in self.driver.current_url

    @pytest.mark.UI
    @allure.feature('Main page')
    def test_go_to_smtp_wikipedia(self, auto):
        """Проверка перехода по кнопке под надписью 'Lets talk about SMTP?'.
           Логинемся с помощью фикстуры auto.
           Ожидаемый результат - переходим на страницу 'https://ru.wikipedia.org/wiki/SMTP'."""
        with allure.step('Кликаем по кнопке под надписью "Lets talk about SMTP?"'):
            self.main_page.go_to_smtp_wikipedia()
        with allure.step('Сравнием url с ожидаемым'):
            self.base_page.screenshot("screen_1")
            assert "https://ru.wikipedia.org/wiki/SMTP" == self.driver.current_url


class TestMock(BaseCase):
    @pytest.mark.UI
    @allure.feature('Mock')
    def test_mock_existing(self, new_user):
        """Проверка появления vk id для пользователя, который есть в моке.
           Ожидаемый результат - появление vk id в правом верхнем углу главной страницы."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Добавляем созданного пользователя в мок'):
            id = randint(1, 10000)
            requests.post('http://0.0.0.0:5555/vk_id/add_user', data={"name": username, "id": id})
        with allure.step('Логинемся с валидными данными'):
            self.login_page.login(username, password)
        with allure.step('Пытаемся найти локатор с VK ID'):
            self.base_page.screenshot("screen_1")
            assert self.base_page.is_vk_id_presented(self.main_page.locators.VK_ID)

    @pytest.mark.UI
    @allure.feature('Mock')
    def test_mock_not_existing(self, new_user):
        """Проверка отсутствия vk id для пользователя, которого нет в моке.
           Ожидаемый результат - отсутствие vk id в правом верхнем углу главной страницы."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.login_page.login(username, password)
        with allure.step('Пытаемся найти локатор с VK ID'):
            self.base_page.screenshot("screen_1")
            assert not self.base_page.is_vk_id_presented(self.main_page.locators.VK_ID)
