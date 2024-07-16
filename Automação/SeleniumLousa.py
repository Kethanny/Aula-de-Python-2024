from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

import time

browser = Firefox()

link = "https://www.jogajuntoinstituto.org/"

browser.get(link)
