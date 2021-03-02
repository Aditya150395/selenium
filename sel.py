from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.implicitly_wait(8)

browser.get("https://www.naukri.com/")
a = browser.find_element_by_xpath('//*[@id="login_Layer"]/div').click()
user = browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[2]/input').send_keys('anshsharmaindia55@gmail.com')
passw = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/form/div[3]/input').send_keys('8882127771')
submit = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/form/div[6]/button').click()

