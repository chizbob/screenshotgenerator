#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser= webdriver.Chrome()
browser.get('http://www.redfin.com')

search = browser.find_element(By.XPATH, '//*[@id="search-box-input"]')
search.clear()
search.send_keys("palo alto")
search.send_keys(Keys.RETURN)
time.sleep(4)

browser.close()
