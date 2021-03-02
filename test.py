#!/usr/bin/env python
import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

current_dir = os.path.dirname(os.path.abspath(__file__))
report_images = "{}/py_report_images".format(current_dir)
if not os.path.exists(report_images):
    os.makedirs(report_images)

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
driver.get('https://www.google.com')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.save_screenshot("{}/screenshot.png".format(report_images))
driver.quit()
