# nhớ zoom nhỏ hết cở lại nha

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
n = int(input('nhập số lần muốn đánh giá: '))
driver = webdriver.Chrome("D:\CodeNguon\selenium\chromedriver.exe")
driver.get("https://sv.iuh.edu.vn/sinh-vien-dang-nhap.html")
driver.maximize_window()
driver.find_element(By.ID, 'UserName').send_keys('21011801')
driver.find_element(By.ID, 'Password').send_keys('0889299883')
time.sleep(10)
count = 0
for i in range(1, n+1):
        j = driver.find_element(By.XPATH, '//*[@id="contnet"]/div/div[2]/div/div/div[2]/div[1]/a').click()
        time.sleep(2)
        tagets = driver.find_elements(By.XPATH, '//*[@id="form0"]/div/div[1]/div/ul/li[5]/label')
        time.sleep(2)
        for j in tagets:
            time.sleep(1)
            u = j.find_element(By.TAG_NAME, 'span').click()
            if count == 5:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            count += 1
        time.sleep(2)
        s = driver.find_element(By.XPATH, '//*[@class="input-ykien"]').send_keys('không')
        time.sleep(2)
        driver.find_element(By.ID, 'btnGui').click()
        time.sleep(10)
        
    