import datetime
import logging
import os

import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utilities.global_variables import GlobalVariables

logging.basicConfig(level=logging.INFO)


class LoginError(RuntimeError):
    pass


class Login():
    tours_test_url = 'http://newtours.demoaut.com/'


class BaseUI():
    global driver

    def launch_browser(self):
		# instantiate a chrome options object so you can set the size and headless preference
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--window-size=1920x1080")

		# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
		# current directory
		chrome_driver = os.getcwd() +"\\chromedriver.exe"

		# go to Google and click the I'm Feeling Lucky button
		driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

	
	
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver.implicitly_wait(30)
        #driver.maximize_window()
        driver.get(Login.tours_test_url)
        return driver

    def get_date_time(self):
        """Return date_time"""
        dt_format = '%Y%m%d_%H%M%S'
        return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)

    def take_screenshot(self, screenshot_name):
        date_time = self.get_date_time()
        if not os.path.exists(GlobalVariables.screenshot_path):
            os.makedirs(GlobalVariables.screenshot_path)
        pic = pyautogui.screenshot()
        pic.save(GlobalVariables.screenshot_path + '\\' + screenshot_name + date_time + '.png')

    def close_browser(self, driver):
        driver.quit()

    def login_application(self, driver, login_type):
        if login_type not in Login.logins_dict.keys():
            logging.info(" Entered In valid login type")
            raise LoginError("account type not in our list")

        username, password = Login.logins_dict[login_type]
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "#login").click()
        return
