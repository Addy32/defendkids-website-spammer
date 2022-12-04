from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import undetected_chromedriver as uc
import random

location = open("locations.txt", "r")
names_last = open("names_last.txt", "r")
names_first = open("names_first.txt", "r")
domains = open("domains.txt", "r")
nameFirstList = names_last.read().splitlines()
nameLastList = names_first.read().splitlines()
locationList = location.read().splitlines()
domainList = domains.read().splitlines()
count = 0
x = True

while True:
    if x:
        name_first = nameFirstList[random.randint(0,(len(nameFirstList)-1))]
        name_last = nameLastList[random.randint(0,(len(nameLastList)-1))]
        name = name_first + " " + name_last
        domain = domainList[random.randint(0,(len(domainList)-1))]
        email = [name_first, name_last][random.randint(0,1)] + str(random.randint(0, 99)) + '@' + domain

        location = locationList[random.randint(0,(len(locationList)-1))]
        driver = uc.Chrome()
        driver.get("https://www.defendkidstx.com#popup")
        open = False
        while open == False:
            if "Defend" in driver.title:
                inputName = driver.find_element(By.ID, 'et_pb_contact_name_0')
                inputName.send_keys(name)
                inputName = driver.find_element(By.ID, 'et_pb_contact_email_0')
                inputName.send_keys(email)
                inputName = driver.find_element(By.ID, 'et_pb_contact_location_of_show_0')
                inputName.send_keys(location)
                time.sleep(1)
                button = driver.find_element(By.NAME, 'et_builder_submit_button')
                ActionChains(driver).click(button).perform()
                time.sleep(4)
                driver.close()
                open = True

            
        count = count + 1
        print(x)