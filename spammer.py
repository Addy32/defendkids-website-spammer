from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import undetected_chromedriver as uc
import random
from names import get_full_name

location = open("locations.txt", "r")
names = open("name.txt", "r")
domain = open("domain.txt", "r")
complant = open("crazy_talk.txt", "r")
nameList = names.read().splitlines()
locationList = location.read().splitlines()
domainList = domain.read().splitlines()
complantList = complant.read().splitlines()
count = 0
x = True

while True:
    if x:
        name = get_full_name()
        domain = domainList[random.randint(0,(len(domainList)-1))]
        if random.randint(0,1) == 0:
            f_name, l_name = name.split(' ')[0], name.split(' ')[1]
            email = f_name + '.' + l_name + str(random.randint(100, 999)) + '@' + domain
        else:
            email = name.split()[random.randint(0,1)] + '@' + domain
        print(email)
        complant = complantList[random.randint(0,(len(complantList)-1))]
        location = locationList[random.randint(0,(len(locationList)-1))]
        driver = uc.Chrome()
        driver.get("https://www.defendkidstx.com#popup")
        open = False
        while open == False:
            if "Defend" in driver.title:
                time.sleep(0.1)
                inputName = driver.find_element(By.ID, 'et_pb_contact_name_0')
                inputName.send_keys(name)
                time.sleep(0.5)
                inputName = driver.find_element(By.ID, 'et_pb_contact_email_0')
                inputName.send_keys(email)
                time.sleep(0.5)
                inputName = driver.find_element(By.ID, 'et_pb_contact_location_of_show_0')
                inputName.send_keys(location)
                time.sleep(0.5)
                if 5 == random.randint(0,5):
                    inputName = driver.find_element(By.ID, 'et_pb_contact_other_info_0')
                    inputName.send_keys(complant)
                time.sleep(2)
                button = driver.find_element(By.NAME, 'et_builder_submit_button')
                ActionChains(driver).click(button).perform()
                time.sleep(10)
                driver.close()
                open = True

            
        count = count + 1
        print(count)
