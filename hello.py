import sys
import os
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/mnt/c/workspace/pydev/chromedriver.exe')
driver.get("https://www.yahoo.co.jp/")
print(driver.title)