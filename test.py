from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox(executable_path='./geckodriver')
web = input('enter website to automate: ')
driver.get(web)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="mod-header-1"]/div[1]/div[6]/ul/li[5]/div[2]').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="sociable_connect"]/div[3]/div[1]').click()
username = input('enter your your username: ')
password = int(input('enter your password: '))
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_xpath('//*[@id="main_login"]/div[3]/div[5]').click()

time.sleep(4)
choice = input('enter your property type: ')
time.sleep(5)
if choice == 'rent':
    driver.find_element_by_xpath('//*[@id="mod-homeController-1"]/section[1]/div[1]/div/div[2]/ul/li[2]/span').click()
elif choice == 'buy':
    driver.find_element_by_xpath('//*[@id="mod-homeController-1"]/section[1]/div[1]/div/div[2]/ul/li[1]/span').click()
elif choice == 'agent':
    driver.find_element_by_xpath('//*[@id="mod-homeController-1"]/section[1]/div[1]/div/div[2]/ul/li[3]/span').click()
else:
    print('invalid')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="homePageSearchBox"]/div/div[2]/input').click()
time.sleep(4)
location = input('enter your location')

driver.find_element_by_xpath('//*[@id="homePageSearchBox"]/div/div[2]/input').send_keys(location)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="homePageSearchBox"]/div/div[4]/ul[1]/li[1]/div/div/div[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="homeSearchWrapper"]/div[3]/span[2]').click()

print('1 for rent')
print('2 for buy')

while True:
    select = input('press(1,2):')
    if select == '1':
        url = driver.find_elements_by_xpath("//div[@class='title-line ']/a")
        urls = []
        for item in url:
            b = item.get_attribute('href')
            urls.append(b)

        for i in urls:
            time.sleep(3)
            driver.get(i)
            time.sleep(4)
            name = driver.find_element_by_xpath("(//span[@class='type'])[1]").text
            price = driver.find_element_by_xpath("(//span[@class='val'])[1]").text
            desc = driver.find_element_by_xpath("//div[@class='clearfix desc-text']").text
            filename = name + '.png'
            time.sleep(3)
            driver.execute_script("window.scrollTo(1350, 1550)")
            time.sleep(5)
            driver.save_screenshot(filename)
            print(name, price, desc)
    elif select == '2':
        links = driver.find_elements_by_xpath("//div[@class='title-line ']/a")
        link = []
        for x in links:
            c = x.get_attribute('href')
            link.append(c)
        for j in link:
            time.sleep(4)
            driver.get(j)
            time.sleep(4)
            nme = driver.find_element_by_xpath("//h1[@class='type-wrap']").text
            amount = driver.find_element_by_xpath("(//span[@class='val'])[2]").text
            description = driver.find_element_by_xpath("//div[@class='clearfix desc-text']").text
            filename = nme + '.png'
            driver.execute_script('window.scrollTo(1350,1550)')
            time.sleep(5)
            driver.save_screenshot(filename)
            print(nme, amount, description)

    break

