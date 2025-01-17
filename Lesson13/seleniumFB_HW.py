from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()
chrome.get('https://zh-tw.facebook.com/')

inputbar = chrome.find_element(By.CLASS_NAME, 'inputtext._55r1._6luy')
inputbar.send_keys('your Email account')
inputbar = chrome.find_element(By.CLASS_NAME, 'inputtext._55r1._6luy._9npi')
inputbar.send_keys('your PASSWORD')
chrome.find_element(By.CLASS_NAME, '_42ft._4jy0._6lth._4jy6._4jy1.selected._51sy').click()
time.sleep(10)
