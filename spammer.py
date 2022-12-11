from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import undetected_chromedriver as uc
import random
from faker import Faker
import string
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
# model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
complaintList = [
    "There's a drag show in town and it has to be stopped. This will cause society to collapse. Write a paragraph explaining why.",
    "There's an event coming up that's going make everyone become transgender if we don't stop it. Write a paragraph about what will happen if everyone becomes trans.",
    "Write a paragraph planning an event to end transphobia."
    "I saw a group of suspicious looking transgender people the other day. They looked like they were plotting something evil. Write a letter to the newspaper explaining why they need to be stopped."
]

fake = Faker()
domain = open("domain.txt", "r")
domainList = domain.read().splitlines()


def generate_address():
    if random.random() < .8:
        address = fake.street_address()
        if random.random() < .2:
            # Append a state to the address
            address = address + " " + fake.state()
    else:
        # Use the langauge model to generate the address so they are harder to filter out
        outputs = model.generate(
            tokenizer.encode("question: what's the address of the coolest queer club in town?", return_tensors="pt"),
            max_length=12, do_sample=True, repetition_penalty=1.5, temperature=1.2, top_p=0.95, top_k=50)
        address = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Randomly add a club name
    if random.random() < .3:
        outputs = model.generate(
            tokenizer.encode("question: what's the name of the coolest queer club in town?", return_tensors="pt"),
            max_length=6, do_sample=True, repetition_penalty=1.5, temperature=1.2, top_p=0.95, top_k=50)
        club_name = tokenizer.decode(outputs[0], skip_special_tokens=True)
        address = club_name.title() + " at " + address

    # remove punctuation
    address = address.translate(str.maketrans('', '', string.punctuation))
    return address


count = 0
x = True

while True:
    if x:

        name = fake.name()
        domain = random.choice(domainList)
        domain = random.choice(domainList)
        if random.randint(0,1) == 0:
            f_name, l_name = name.split(' ')[0], name.split(' ')[1]
            email = f_name + '.' + l_name + str(random.randint(100, 999)) + '@' + domain
        else:
            email = name.split()[random.randint(0,1)] + '@' + domain
        # email = fake.ascii_free_email()

        inputs = tokenizer.encode(random.choice(complaintList), return_tensors="pt")
        outputs = model.generate(
            inputs,
            max_length=100,
            do_sample=True,
            repetition_penalty=1.5, temperature=1.2,
            top_p=0.95, top_k=50)
        complaint = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # complaint = fake.paragraph(nb_sentences=5)

        location = generate_address()

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
                inputName = driver.find_element(By.ID, 'et_pb_contact_other_info_0')
                inputName.send_keys(complaint)
                time.sleep(2)
                button = driver.find_element(By.NAME, 'et_builder_submit_button')
                ActionChains(driver).click(button).perform()
                time.sleep(10)
                driver.close()
                open = True

            
        count = count + 1
        print(f'{count} transphobes annoyed: {name}, {email}, {location}, {complaint}')
