import pytest
import allure
from base_api import BaseCase


class TestApi(BaseCase):
    @pytest.mark.API
    @allure.feature('Api app status')
    def test_status_app(self):
        """Проверка статуса приложения.
           Ожидаемый результат: действие выполнено - статус код 200."""
        with allure.step('Делаем запрос в приложение'):
            response = self.client.status()
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 200

    @pytest.mark.API
    @allure.feature('Api login')
    def test_negative_login(self):
        """Проверка авторизации незарегестрированного пользователя.
           Ожидаемый результат: пользователь не авторизован - статус код 401."""
        with allure.step('Генерируем валидный логин и пароль'):
            username = self.builder.password()
            password = self.builder.login()
        with allure.step('Логинемся с невалидными данными'):
            response = self.client.login(username, password)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 401

    @pytest.mark.API
    @allure.feature('Api login')
    def test_valid_login_negative_active(self, new_user):
        """Проверка присутствия авторизационного пользователя на странице после регистрации.
           Ожидаемый результат: поле active - 0."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
        with allure.step('Сверяем значение поля active с ожидаемым'):
            assert (self.mysql_builder.get_user(username))['active'] == 0

    @pytest.mark.API
    @allure.feature('Api login')
    def test_valid_login_active(self, new_user):
        """Проверка присутствия авторизационного пользователя на странице после регистрации и входа.
           Ожидаемый результат: поле active - 1."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.client.login(username, password)
        with allure.step('Сверяем значение поля active с ожидаемым'):
            assert (self.mysql_builder.get_user(username))['active'] == 1

    @pytest.mark.API
    @allure.feature('Api login')
    def test_login_block_user(self, new_user):
        """Проверка авторизации заблокированного пользователя.
           Ожидаемый результат: пользователь не авторизован - статус код 401."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.client.login(username, password)
        with allure.step('Блокируем пользователя'):
            self.client.block_user(username)
        with allure.step('Повторно логинемся'):
            response = self.client.login(username, password)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 401

    @pytest.mark.parametrize(
        'username, password',
        [pytest.param('', 'passwordvalid'), pytest.param('loginvalid', ''), pytest.param('', '')]
                            )
    @pytest.mark.UI
    @allure.feature('Api login')
    def test_negative_reg_empty_fields(self, username, password):
        """Проверка авторизации с пустым полями:
           1. username
           2. password
           3. username и password
           Ожидаемый результат: плохой запрос - статус код 400."""
        with allure.step('Логинемся с невалидными данными'):
            response = self.client.login(username, password)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 400

    @pytest.mark.API
    @allure.feature('Api reg')
    def test_valid_reg(self, new_user):
        """Проверка доступа зарегестрированного пользователя.
           Ожидаемый результат: поле access - 1."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
        with allure.step('Сверяем значение поля access с ожидаемым'):
            assert (self.mysql_builder.get_user(username))['access'] == 1

    @pytest.mark.API
    @allure.feature('Api reg')
    def test_valid_reg_access(self):
        """Проверка регистрации пользователя.
           Ожидаемый результат: сущность создана - статус код 201."""
        with allure.step('Генерируем валидный логин, пароль и email'):
            username = self.builder.password()
            email = self.builder.email()
            password = self.builder.login()
        with allure.step('Регистрируемся с валидными данными'):
            response = self.client.registration(username, password, email)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 201

    @pytest.mark.API
    @allure.feature('Api reg')
    def test_reg_existing_username(self, new_user):
        """Проверка регистрации пользователя с уже зарегестрированным логином.
           Ожидаемый результат: сущность существует - статус код 304."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
        with allure.step('Генерируем валидный пароль и email'):
            email = self.builder.email()
            password = self.builder.password()
        with allure.step('Регистрируемся с валидными данными'):
            response = self.client.registration(username, password, email)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 304

    @pytest.mark.API
    @allure.feature('Api reg')
    def test_reg_existing_email(self, new_user):
        """Проверка регистрации пользователя с уже зарегестрированным email.
           Ожидаемый результат: сущность существует - статус код 304."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            email = new_user.email
        with allure.step('Генерируем валидный логин и пароль'):
            username = self.builder.login()
            password = self.builder.login()
        with allure.step('Регистрируемся с валидными данными'):
            response = self.client.registration(username, password, email)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 304

    @pytest.mark.API
    @allure.feature('Api delete')
    def test_delete_user(self, new_user):
        """Проверка удаления зарегестированного невошедшего пользователя.
           Ожидаемый результат: сущность удалена - статус код 204."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
        with allure.step('Удаляем пользователя'):
            response = self.client.delete_user(username)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 204

    @pytest.mark.API
    @allure.feature('Api delete')
    def test_delete_login_user(self, new_user):
        """Проверка удаления зарегестированного вошедшего пользователя.
           Ожидаемый результат: сущность удалена - статус код 204."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.client.login(username, password)
        with allure.step('Удаляем пользователя'):
            response = self.client.delete_user(username)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 204

    @pytest.mark.API
    @allure.feature('Api block')
    def test_block_user(self, new_user):
        """Проверка блокирования зарегестированного невошедшего пользователя.
           Ожидаемый результат: действие выполнено - статус код 200."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
        with allure.step('Блокируем пользователя'):
            response = self.client.block_user(username)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 200

    @pytest.mark.API
    @allure.feature('Api block')
    def test_block_login_user(self, new_user):
        """Проверка блокирования зарегестированного вошедшего пользователя.
           Ожидаемый результат: действие выполнено - статус код 200."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.client.login(username, password)
        with allure.step('Блокируем пользователя'):
            response = self.client.block_user(username)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 200

    @pytest.mark.API
    @allure.feature('Api block')
    def test_block_user_access(self, new_user):
        """Проверка блокирования зарегестированного невошедшего пользователя.
           Ожидаемый результат: поле access - 1."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
        with allure.step('Блокируем пользователя'):
            self.client.block_user(username)
        with allure.step('Сверяем значение поля access с ожидаемым'):
            assert (self.mysql_builder.get_user(username))['access'] == 0

    @pytest.mark.API
    @allure.feature('Api block')
    def test_block_login_user_access(self, new_user):
        """Проверка блокирования зарегестированного вошедшего пользователя.
           Ожидаемый результат: поле access - 0."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.client.login(username, password)
        with allure.step('Блокируем пользователя'):
            self.client.block_user(username)
        with allure.step('Сверяем значение поля access с ожидаемым'):
            assert (self.mysql_builder.get_user(username))['access'] == 0

    @pytest.mark.API
    @allure.feature('Api block')
    def test_block_and_unblock_login_user(self, new_user):
        """Проверка блокирования и разблокирования зарегестированного вошедшего пользователя.
           Ожидаемый результат: действие выполнено - статус код 200."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.client.login(username, password)
        with allure.step('Блокируем пользователя'):
            self.client.block_user(username)
        with allure.step('Разблокируем пользователя'):
            response = self.client.unblock_user(username)
        with allure.step('Сверяем полученный статус код с ожидаемым'):
            assert response.status_code == 200

    @pytest.mark.API
    @allure.feature('Api block')
    def test_block_and_unblock_login_user_access(self, new_user):
        """Проверка блокирования и разблокирования зарегестированного вошедшего пользователя.
           Ожидаемый результат: поле access - 1."""
        with allure.step('Добавляем пользователя с помощью базы данных'):
            username = new_user.username
            password = new_user.password
        with allure.step('Логинемся с валидными данными'):
            self.client.login(username, password)
        with allure.step('Блокируем пользователя'):
            self.client.block_user(username)
        with allure.step('Разблокируем пользователя'):
            self.client.unblock_user(username)
        with allure.step('Сверяем значение поля access с ожидаемым'):
            assert (self.mysql_builder.get_user(username))['access'] == 1

