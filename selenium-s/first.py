from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://192.168.0.247')
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/form/div[2]/div/div/input").send_keys("test")
driver.find_element_by_xpath("/html/body/div/form/div[3]/div/div/input").send_keys("qwer1234")
driver.find_element_by_xpath("/html/body/div/form/button").click()
