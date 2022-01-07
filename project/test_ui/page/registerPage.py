from selenium.webdriver.common.by import By

class RegisterPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_email_register = '//*[@id="__next"]/div[1]/div/div[2]/form/div[1]/div/div/input'
        self.input_username = '//*[@id="__next"]/div[1]/div/div[2]/form/div[2]/div/div/input'
        self.button_daftar = '//*[@id="__next"]/div[1]/div/div[2]/form/div[3]/button'

    def enter_email_register(self, email):
        self.driver.find_element(By.XPATH,self.input_email_register).clear()
        self.driver.find_element(By.XPATH,self.input_email_register).send_keys(email)

    def enter_username(self, username):
        self.driver.find_element(By.XPATH,self.input_username).clear()
        self.driver.find_element(By.XPATH,self.input_username).send_keys(username)

    def click_button_daftar(self):
        self.driver.find_element(By.XPATH,self.button_daftar).click()