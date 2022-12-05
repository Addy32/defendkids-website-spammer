from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import undetected_chromedriver as uc
import random
from names import get_full_name

location = open("locations.txt", "r")
domain = open("domain.txt", "r")
locationList = location.read().splitlines()
domainList = domain.read().splitlines()
count = 0
x = True

while True:
    if x:
        name = get_full_name()
        domain = domainList[random.randint(0,(len(domainList)-1))]
        email = name.split()[random.randint(0,1)] + '@' + domain

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