from selenium import webdriver
import time
drver_path = r"D:\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=drver_path)
driver.get('https://www.baidu.com/')

# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
inputTag = driver.find_element_by_css_selector("")
inputTag.send_keys('python')

# time.sleep(5)
# driver.close()