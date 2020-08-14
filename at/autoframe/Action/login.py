# -*- coding:utf-8 -*-

import time
from selenium import webdriver
from Util.Log import *
from Util.FormatTime import data_time_chinese
from PageProject.login_page import *

def login(driver,username,password):
    driver.get("https://mail.126.com")
    time.sleep(2)
    lp = LoginPage(driver)
    lp.lbnormalbutton_click()
    lp.switch_to_frame()
    time.sleep(2)
    lp.input_username(username)
    lp.input_password(password)
    lp.loginbutton_click()
    time.sleep(2)
    info("Login Successfully!")
    print data_time_chinese()

if __name__ == "__main__":
    driver = webdriver.Firefox(executable_path = "D:\\geckodriver")
    login(driver,"xxx","xxx")