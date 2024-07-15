from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

import time

browser = Firefox()

link = "https://google.com"

browser.get(link)

btn_add_element = browser.find_element(By.NAME, "q")