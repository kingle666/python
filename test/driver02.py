from selenium import webdriver
import time

drver_path = r"D:\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=drver_path)

driver.get('https://www.douban.com/')
rememberBtn = driver.find_element_by_name('remember')
rememberBtn.click()