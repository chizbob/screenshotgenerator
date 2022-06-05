#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


browser= webdriver.Chrome()
browser.get('http://www.redfin.com')

search = browser.find_element(By.XPATH, '//*[@id="search-box-input"]')
search.clear()
search.send_keys("palo alto")
search.send_keys(Keys.RETURN)
time.sleep(5)
select_house = Select(browser.find_element(By.XPATH, '//*[@id="sidepane-header"]/div/div[1]/form/div[3]/div/svg'))
select.select_by_value("House")


done_button = driver.find_element(By.XPATH,'//*[@id="sidepane-header"]/div/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/button[2]/span')
done_button.submit();
time.sleep(7)



browser.close()
