from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://vinmart.co/bo-my-xay-500gram-us-minced-ground-beef-s9273739221.html")

taget = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/div[2]/div[3]')
# for i in taget:
#     print(i.text)
print(taget.text)