# -*- coding:utf-8 -*-

from selenium import webdriver
from Util.Log import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
from login import *

def visit_address_page(driver):
    hp = HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(5)

if __name__ == "__main__":
    driver = webdriver.Firefox(executable_path = "D:\\geckodriver")
    login(driver,"xxx","xxx")
    visit_address_page(driver)
