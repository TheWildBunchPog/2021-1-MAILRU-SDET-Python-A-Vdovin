from selenium.webdriver.common.by import By


class BasePageLocators:
    ENTER = (By.XPATH, "//*[contains(@class, 'responseHead-module-button')]")
    LOGIN = (By.XPATH, "//*[@name='email']")
    PASSWORD = (By.XPATH, "//*[@type='password']")
    LOG_IN = (By.XPATH, "//div[contains(@class,'authForm') and contains(text(), 'Войти')]")
    INVALID_LOGIN_OR_PASSWORD = (By.XPATH, "//div[contains(@class,'formMsg_text') and contains(text(), 'Invalid login or password')]")


class MainPageLocators(BasePageLocators):
    CAMPAIGNS = (By.XPATH, '//a[@href="/dashboard"]')
    AUDIENCE = (By.XPATH, '//a[@href="/segments"]')


class CampaignPageLocators(BasePageLocators):
    CREATE_CAMPAIGN = (By.XPATH, "//div[contains(@class, 'dashboard-module-createButtonWrap')]/div/div")
    CREATE_FIRST_CAMPAIGN = (By.XPATH, "//*[contains(@href, '/campaign/new')]")
    TRAFFIC = (By.XPATH, "//div[contains(@class, '_traffic')]")
    ENTER_LINK = (By.XPATH, "//input[contains(@data-gtm-id,'ad_url_text')]")
    NAME_CAMPAIGN = (By.XPATH, '//div[contains(@class,"input_campaign-name")]//input')
    CLEAR_NAME_CAMPAIGN = (By.XPATH, '//div[contains(@class, "input__clear")]')
    BANNER = (By.XPATH, '//div[@id="patterns_4"]')
    UPLOAD_IMAGE = (By.XPATH, '//input[@type="file" and @data-test="image_240x400"]')
    SAVE_AD = (By.XPATH, '//div[contains(@data-test,"submit_banner_button")]')
    CONFIRM_CREATE_CAMPAIGN = (By.XPATH, '//div[contains(@class, "footer")]/button')
    ACTION_MENU = (By.XPATH, " //*[contains(@class, 'select-module-itemInner') and text()='Действия']")
    DELETE_CAMPAIGN = (By.XPATH, "//li[contains(@class,'optionsList-module-option') and @title='Удалить']")


class AudiencePageLocators(MainPageLocators):
    CREATE_FIRST_SEGMENT = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    CREATE_SEGMENT = (By.XPATH, '//button[@class="button button_submit"]')
    APPS_AND_GAMES = (By.XPATH, '//div[contains(@class,"adding-segments-modal__block-left")]/div[8]')
    CHECK_BOX_PROPERTY = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    ADD_SEGMENT = (By.XPATH, '//div[contains(@class, "adding-segments-modal__footer")]/div[1]/button/div')
    INPUT_NAME_SEGMENT = (By.XPATH, '//div[contains(@class,"input_create-segment-form")]//input')
    INPUT_SEARCH_SEGMENT = (By.XPATH, '//input[@type="text"]')
    DELETE_SEGMENTS = (By.XPATH, '//span[contains(@class,"icon-cross")]')
    SUBMIT_DELETE = (By.XPATH, '//div[@class="button__text" and contains(text(), "Удалить")]')
