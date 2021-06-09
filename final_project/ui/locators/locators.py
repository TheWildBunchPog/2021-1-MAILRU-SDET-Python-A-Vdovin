from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_SUBMIT = (By.ID, 'submit')
    GO_TO_CREATE_ACCOUNT = (By.XPATH, '//a[contains(@href,"/reg")]')
    INVALID_USERNAME_OR_PASSWORD = (By.XPATH, '//div[contains(text(),"Invalid username or password")]')
    INCORRECT_USERNAME_LENGTH = (By.XPATH, '//div[contains(text(),"Incorrect username length")]')
    ACCOUNT_BLOCK = (By.XPATH, '//div[contains(text(),"Ваша учетная запись заблокирована")]')
    LOGOUT = (By.XPATH, '//a[text()= "Logout"]')


class RegistrationPageLocators:
    USERNAME_FIELD = (By.ID, 'username')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.XPATH, '//input[contains(@id,"password")]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[contains(@id,"confirm")]')
    ACCEPT = (By.ID, 'term')
    REGISTER_SUBMIT = (By.ID, 'submit')
    GO_TO_LOG_IN = (By.XPATH, '//a[contains(@href,"/login")]')
    GO_TO_CREATE_ACCOUNT = (By.XPATH, '//a[contains(@href,"/reg")]')
    USER_ALREADY_EXISTS = (By.XPATH, '//div[contains(text(),"User already exist")]')
    INCORRECT_USERNAME_LENGTH = (By.XPATH, '//div[contains(text(),"Incorrect username length")]')
    INCORRECT_PASSWORD_LENGTH = (By.XPATH, '//div[contains(text(),"Incorrect password length")]')
    INVALID_EMAIL_ADDRESS = (By.XPATH, '//div[contains(text(),"Invalid email address")]')
    INCORRECT_EMAIL_LENGTH = (By.XPATH, '//div[contains(text(),"Incorrect email length")]')
    PASSWORDS_MUST_MATCH = (By.XPATH, '//div[contains(text(),"Passwords must match")]')


class MainPageLocators:
    HOME = (By.XPATH, '//a[contains(text(),"HOME")]')
    PYTHON = (By.XPATH, '//a[@href="https://www.python.org/"]')
    PYTHON_HISTORY = (By.XPATH, '//a[contains(text(),"Python history")]')
    ABOUT_FLASK = (By.XPATH, '//a[contains(text(),"About Flask")]')
    LINUX = (By.XPATH, '//a[contains(text(),"Linux")]')
    DOWNLOAD_CENTOS = (By.XPATH, '//a[contains(text(),"Download Centos7")]')
    NETWORK = (By.XPATH, '//a[contains(text(),"Network")]')
    WIRESHARK_NEWS = (By.XPATH, '//a[contains(text(),"News")]')
    WIRESHARK_DOWNLOAD = (By.XPATH, '//a[text()= "Download"]')
    TCPDUMP_EXAMPLES = (By.XPATH, '//a[contains(text(),"Examples")]')
    API_WIKIPEDIA = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    FUTURE_OF_INTERNET = (By.XPATH,
        '//a[@href="https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/"]')
    SMTP_WIKIPEDIA = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')
    VK_ID = (By.XPATH, '//li[contains(text(),"VK ID")]')
    LOGOUT = (By.XPATH, '//a[text()= "Logout"]')
