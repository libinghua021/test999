# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
import time

#获取单个页面元素对象
def getElement(driver,locateType,locateExpression):
    try:
        element = WebDriverWait(driver,5).until(lambda x: x.find_element(by = locateType,value = locateExpression))
        return element
    except Exception,e:
        raise e

#获取多个相同页面元素对象，以list返回
def getElements(driver,locateType,locateExpression):
    try:
        element = WebDriverWait(driver,5).until(lambda x: x.find_elements(by = locateType,value = locateExpression))
        return element
    except Exception,e:
        raise e

if __name__ == "__main__":
    from selenium import webdriver
    #进行单元测试
    driver = webdriver.Firefox(executable_path = "D:\\geckodriver")
    driver.maximize_window()
    driver.get("https://mail.126.com/")
    time.sleep(2)
    lb = getElement(driver,"id","lbNormal")
    print lb
    driver.quit()