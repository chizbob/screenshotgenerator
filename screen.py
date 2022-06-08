#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from PIL import Image


#go to linkedin site
driver= webdriver.Chrome()
driver.get('http://www.linkedin.com')

#login to the site
driver.find_element(By.XPATH, '/html/body/nav/div/a[2]').click()
driver.find_element(By.ID, 'username').send_keys('sokim@linkedin.com')
driver.find_element(By.ID, 'password').send_keys('rlatnwjd12')
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(7)

#take a screenshot

driver.save_screenshot('home_us.png')
screenshot = Image.open('home_us.png')

#change language setting
# #go to the profile
# search = browser.find_element(By.XPATH, '//*[@id="search-box-input"]')
# search.clear()
# search.send_keys("palo alto")
# search.send_keys(Keys.RETURN)
# time.sleep(5)
#
# #go to certifications, view all licenses and certifications
# select_house = Select(browser.find_element(By.XPATH, '//*[@id="sidepane-header"]/div/div[1]/form/div[3]/div[1]/span'))
# select.select_by_value("House")
#
# #screen capture and save

#unit test
#done_button.submit();
time.sleep(2)
driver.close()
