import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class HackerEarth_Test(unittest.TestCase):

    def setUp(self):

        self.URL = "https://hackerearth.com/"
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1440, 900)
        self.driver.get(self.URL)

    def test_login(self):

        login_form_xPath = '//a[@target="login-modal"]'
        loginButton_xpath = '//input[@name = "submit"]'
        emailField_xpath =  '//input[@name="login"]'
        passField_xpath = '//input[@name="password"]'
        email = 'ffi69465@posdz.com'
        password = 'TestTest'
        login_driver = self.driver
        login_form = login_driver.find_element_by_xpath(login_form_xPath).click()
        emailField = WebDriverWait(login_driver, 10).until(lambda login_driver: login_driver.find_element_by_xpath(emailField_xpath))
        passwordField = WebDriverWait(login_driver, 10).until(lambda login_driver: login_driver.find_elements_by_xpath(passField_xpath ))
        loginButton = WebDriverWait(login_driver, 10).until(lambda login_driver: login_driver.find_elements_by_xpath(loginButton_xpath))

        #Adding email field
        emailField.clear()
        emailField.send_keys(email)

        #Adding Password Field
        passwordField[1].clear()
        passwordField[1].send_keys(password)

        #Login button clicked
        loginButton[1].click()


    def tearDown(self):
        self.driver.quit()
        return


if __name__ == '__main__':

    unittest.main()

