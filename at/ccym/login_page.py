# -*- coding:utf-8 -*-

from selenium import webdriver

wd = webdriver.Chrome()
wd.get('http://192.168.0.241:3003')
# wd.maximize_window()
wd.find_element_by_xpath("//div[@id='app']/div/div[1]/div[1]/div/div[1]/div/div[2]").click()
wd.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/img[1]')
# a = wd.find_element_by_class_name('toScan')
# wd.execute_script(a.click())
# wd.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/input").send_keys('13338053699')
# wd.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/input").send_keys('a123456')
# wd.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div[6]").click()