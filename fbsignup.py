from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox(executable_path='/home/aditya/PycharmProjects/facebook/geckodriver')
driver.get('https://www.facebook.com/')
driver.maximize_window()


driver.find_element_by_xpath("//div[@class='_6ltg']/a").click()
time.sleep(4)
driver.find_element_by_xpath("//div[@class='_5dbb']/input").send_keys('Aditya')
driver.find_element_by_name('lastname').send_keys('Sharma')
driver.find_element_by_name('reg_email__').send_keys('8882127771')
driver.find_element_by_name('reg_passwd__').send_keys('8882127771')
driver.find_element_by_name('reg_passwd__').send_keys('8882127771')
day = Select(driver.find_element_by_name('birthday_day'))
day.select_by_visible_text('11')
month = Select(driver.find_element_by_name('birthday_month'))
month.select_by_visible_text('Nov')
year = Select(driver.find_element_by_name('birthday_year'))
year.select_by_visible_text('1995')
driver.find_element_by_name('sex').click()
driver.find_element_by_name('websubmit').click()


#driver.find_element(By.ID,'email').send_keys('8882127771')
#driver.find_element(By.ID, 'pass').send_keys('9958302058')
#time.sleep(3)
#driver.find_element_by_xpath("//div[@class='_6ltg']/button").click()
#driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[3]/a').click()
#driver.find_element_by_id('identify_email').send_keys('8882127771')
#driver.find_element_by_id('did_submit').click()
#driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div[2]/div/form/div/div[3]/div/div[1]').click()
