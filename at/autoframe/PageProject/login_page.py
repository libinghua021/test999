# -*- coding:utf-8 -*-

import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.login_page_items = self.parse_config_file.getItemsFromSection("126mail_login")
        print self.login_page_items

    #获取元素
    def lbnormalbutton(self):
        locateType, locateExpression = self.login_page_items['login_page.lbnormalbutton'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def frame(self):
        locateType, locateExpression = self.login_page_items['login_page.frame'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def username(self):
        locateType, locateExpression = self.login_page_items['login_page.username'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def password(self):
        locateType, locateExpression = self.login_page_items['login_page.password'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def loginbutton(self):
        locateType, locateExpression = self.login_page_items['login_page.loginbutton'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    #操作元素
    def lbnormalbutton_click(self):
        self.lbnormalbutton().click()

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.frame())

    def input_username(self,username):
        self.username().send_keys(username)

    def input_password(self,password):
        self.password().send_keys(password)

    def loginbutton_click(self):
        self.loginbutton().click()


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox(executable_path = "D:\\geckodriver")
    driver.maximize_window()
    driver.get("https://mail.126.com")
    lp = LoginPage(driver)
    # lp.lbnormalbutton().click()
    lp.lbnormalbutton_click()
    time.sleep(1)
    # driver.switch_to.frame(lp.frame())
    lp.switch_to_frame()
    time.sleep(3)
    # lp.username().send_keys("xxx")
    lp.input_username("xxx")
    # lp.password().send_keys("xxx")
    lp.input_password("xxx")
    lp.loginbutton_click()
    time.sleep(5)
    driver.quit()