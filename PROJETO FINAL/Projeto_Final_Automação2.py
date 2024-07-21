from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = Firefox()

try:

    link = 'https://projetofinal.jogajuntoinstituto.org/'
    browser.get(link)


    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys('kethynayane816@gmail.com')


    input_senha = browser.find_element(By.NAME, "password")
    input_senha.send_keys('kethy123')
    input_senha.send_keys(Keys.ENTER)

 
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/section[2]/div/header/button'))
    ).click()

finally:
    browser.quit()