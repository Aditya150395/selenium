from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox(executable_path='/home/aditya/PycharmProjects/facebook/geckodriver')
driver.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="ow324"]/span/span').click()
time.sleep(3)
driver.find_element_by_xpath("(//div[@class='uyYuVb oJeWuf'])[1]/div").click()
time.sleep(4)
driver.find_element_by_name('firstName').send_keys('Aditya')
driver.find_element_by_name('lastName').send_keys('Sharma')
driver.find_element_by_id('username').send_keys('aditya150319965')
driver.find_element_by_name('Passwd').send_keys('8882127771')
driver.find_element_by_name('ConfirmPasswd').send_keys('8882127771')
driver.find_element_by_xpath("(//div[@class='VfPpkd-RLmnJb'])[2]").click()
