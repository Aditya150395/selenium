from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get('https://www.makaan.com/')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="mod-header-1"]/div[1]/div[6]/ul/li[5]/div[2]').click()
driver.implicitly_wait(4)
driver.find_element_by_xpath(
    '/html/body/div[1]/div[5]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]/div[1]').click()
driver.find_element(By.ID, 'username').send_keys('anshsharmaindia55@gmail.com')
driver.find_element(By.ID, 'password').send_keys('8882127771')
driver.find_element_by_xpath(
    '/html/body/div[1]/div[5]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[5]').click()
time.sleep(5)
print('select operation')
print('press 1 for Buy: ')
print('press 2 for Rent: ')
print('press 3 for Agent: ')
while True:
    choice = input('press (1,2,3):')
    if choice == '1':
        driver.find_element_by_xpath(
            '/html/body/div[1]/main/div/section[1]/div[1]/div/div[3]/div[1]/div/div/div/div[2]/input').click()
    elif choice == '2':
        driver.find_element_by_xpath('//*[@id="mod-homeController-1"]/section[1]/div[1]/div/div[2]/ul/li[2]/span').click()
    elif choice == '3':
        driver.find_element_by_xpath('//*[@id="mod-homeController-1"]/section[1]/div[1]/div/div[2]/ul/li[3]/span').click()
    break

driver.find_element_by_xpath(
    '//*[@id="homePageSearchBox"]/div/div[2]/input'
).click()

driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div[1]/div/div[3]/div[1]/div/div/div/div[2]/input').send_keys('Gurgaon')
driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div[1]/div/div[3]/div[1]/div/div/div/div[4]/ul[1]/li[1]/div/div/div[1]').click()

time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div[1]/div/div[3]/div[3]/span[2]').click()

time.sleep(3)

agent = driver.find_elements_by_xpath("//h2[@class='sllrname']/a")
rent = driver.find_elements_by_xpath("//div[@class='seller-info']/a/span")
buy = driver.find_elements_by_xpath("//a[@class='seller-name ']/span")
for i in agent:
    print(i.text)

for j in rent:
    print(j.text)

for k in buy:
    print(k.text)
