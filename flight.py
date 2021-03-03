from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.implicitly_wait(7)
driver.get('https://www.makaan.com/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="mod-header-1"]/div[1]/div[6]/ul/li[5]/div[2]').click()
driver.get('https://www.makaan.com/#loginPopup')

driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]/div[1]').click()

driver.find_element_by_xpath('//*[@id="username"]').send_keys('anshsharmaindia55@gmail.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('8882127771')
driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[5]').click()