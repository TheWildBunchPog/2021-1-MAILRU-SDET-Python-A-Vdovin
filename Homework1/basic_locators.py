from selenium.webdriver.common.by import By


ENTER = (By.XPATH, "//*[contains(@class, 'responseHead-module-button')]")
LOGIN = (By.XPATH, "//*[@name='email']")
PASSWORD = (By.XPATH, "//*[@type='password']")
LOG_IN = (By.XPATH, "//div[contains(@class,'authForm') and contains(text(), 'Войти')]")
MAKE = (By.XPATH, "//*[contains(@href, '/campaign/new')]")
MAIN = (By.XPATH, "//*[contains(@class, 'right-module-userNameWrap')]")
LOG_OUT = (By.XPATH, "//*[contains(@href, '/logout')]")
PROFILE = (By.XPATH, "//*[contains(@href, '/profile')]")
FIO = (By.XPATH, "//*[contains(@maxlength, '100')]")
SAVE = (By.XPATH, "//div[contains(@class,'button__text') and contains(text(), 'Сохранить')]")
BALANCE = (By.XPATH, "//*[contains(@href, '/billing')]")
STATISTIC = (By.XPATH, "//*[contains(@href, '/statistics')]")
SCORE = (By.XPATH, "//*[contains(@value, 'Пополнить счёт')]")
SUMMARY = (By.XPATH, "//*[contains(@href, '/statistics/summary')]")









