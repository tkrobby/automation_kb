import pytest
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from page.registerPage import RegisterPage
from page.OtpPage import OTPPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions() 
        cls.options.add_argument("--disable-blink-features=AutomationControlled")
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.maximize_window()

    def test_register_kitabisa_use_invalid_phone_number_format(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register('69012')
        register.enter_username('firda s')
        time.sleep(2)
        
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[2]/form/div[1]/div/span').text
        print(warning)
        assert warning == "Hanya diisi dengan nomor ponsel atau email yang valid."

    def test_register_kitabisa_use_max_character_phone_number_(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register('08781271281281281821928128')
        register.enter_username('firda s')
        time.sleep(2)
        
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[2]/form/div[1]/div/span').text
        print(warning)
        assert warning == "Hanya diisi dengan nomor ponsel atau email yang valid."

    def test_register_kitabisa_use_invalid_email_format(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register('firda001')
        register.enter_username('firda s')
        time.sleep(2)
        
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[2]/form/div[1]/div/span').text
        print(warning)
        assert warning == "Hanya diisi dengan nomor ponsel atau email yang valid."
        print("test case done")

    def test_register_kitabisa_just_input_space_on_field_emai(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register(' ')
        register.enter_username('firda s')
        time.sleep(2)
        
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[2]/form/div[1]/div/span').text
        print(warning)
        assert warning == "Nomor ponsel atau email tidak boleh kosong."
        print("test case done")

    def test_register_kitabisa_just_input_space_on_field_nama_lengkap(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register('sales@mail.com')
        register.enter_username(' ')
        time.sleep(2)
        
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[2]/form/div[2]/div/span').text
        print(warning)
        assert warning == "Nama lengkap tidak boleh kosong."
        print("test case done")

    def test_register_kitabisa_input_special_character_on_field_nama_lengkap(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register('sales@mail.com')
        register.enter_username('rm -rf /*')
        time.sleep(2)
        
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[2]/form/div[2]/div/span').text
        print(warning)
        assert warning == "Nama lengkap hanya boleh huruf, titik (.) dan apostrof (')."
        print("test case done")

    def test_register_kitabisa_use_invalid_otp(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register('firdanil06@mail.com')
        register.enter_username('nalin s')
        register.click_button_daftar()
        time.sleep(2)

        otpPage = OTPPage(driver)
        time.sleep(2)
        otpPage.enter_otp_1('8')
        otpPage.enter_otp_2('0')
        otpPage.enter_otp_3('2')
        otpPage.enter_otp_4('8')
        otpPage.enter_otp_5('0')
        otpPage.enter_otp_6('6')
        otpPage.click_button_otp()
        time.sleep(5)
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/form/div[1]/div[2]').text
        print(warning)
        assert warning == "Kode verifikasi salah, Silakan coba lagi"
        print("test case done")

    def test_register_kitabisa_use_otp_less_then_6_character(self):
        driver = self.driver
        driver.get("https://accounts.kitabisa.com/register")

        register = RegisterPage(driver)
        register.enter_email_register('firda001@gmail.com')
        register.enter_username('firda s')
        register.click_button_daftar()
        time.sleep(2)

        otpPage = OTPPage(driver)
        time.sleep(2)
        otpPage.enter_otp_1('8')
        otpPage.enter_otp_2('0')
        otpPage.enter_otp_3('2')
        time.sleep(5)
        warning = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/form/div[1]/div[2]').text
        print(warning)
        assert warning == "OTP terlalu pendek (minimal 6 karakter)."
        print("test case done")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Testing Register Completed")

if __name__ == "__main__":
    unittest.main()