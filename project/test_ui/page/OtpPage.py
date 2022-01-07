from selenium.webdriver.common.by import By

class OTPPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_otp_1 = '//*[@id="__next"]/div/div/div[2]/form/div[1]/div/input[1]'
        self.input_otp_2 = '//*[@id="__next"]/div/div/div[2]/form/div[1]/div/input[2]'
        self.input_otp_3 = '//*[@id="__next"]/div/div/div[2]/form/div[1]/div/input[3]'
        self.input_otp_4 = '//*[@id="__next"]/div/div/div[2]/form/div[1]/div/input[4]'
        self.input_otp_5 = '//*[@id="__next"]/div/div/div[2]/form/div[1]/div/input[5]'
        self.input_otp_6 = '//*[@id="__next"]/div/div/div[2]/form/div[1]/div/input[6]'
        self.click_submit_button = '//*[@id="__next"]/div/div/div[2]/form/div[2]/button'

    def enter_otp_1(self, otp_1):
        self.driver.find_element(By.XPATH,self.input_otp_1).clear()
        self.driver.find_element(By.XPATH,self.input_otp_1).send_keys(otp_1)

    def enter_otp_2(self, otp_2):
        self.driver.find_element(By.XPATH,self.input_otp_2).clear()
        self.driver.find_element(By.XPATH,self.input_otp_2).send_keys(otp_2)

    def enter_otp_3(self, otp_3):
        self.driver.find_element(By.XPATH,self.input_otp_3).clear()
        self.driver.find_element(By.XPATH,self.input_otp_3).send_keys(otp_3)

    def enter_otp_4(self, otp_4):
        self.driver.find_element(By.XPATH,self.input_otp_4).clear()
        self.driver.find_element(By.XPATH,self.input_otp_4).send_keys(otp_4)

    def enter_otp_5(self, otp_5):
        self.driver.find_element(By.XPATH,self.input_otp_5).clear()
        self.driver.find_element(By.XPATH,self.input_otp_5).send_keys(otp_5)

    def enter_otp_6(self, otp_6):
        self.driver.find_element(By.XPATH,self.input_otp_6).clear()
        self.driver.find_element(By.XPATH,self.input_otp_6).send_keys(otp_6)

    def click_button_otp(self):
        self.driver.find_element(By.XPATH,self.click_submit_button).click()