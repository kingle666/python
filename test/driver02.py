from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

drver_path = r"D:\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=drver_path)
driver.get('https://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
# submitBtn = driver.find_element_by_id('su')
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag,'python')
# actions.click(submitBtn)
# actions.perform()

for coikie in driver.get_cookies():
    print(coikie)
print('='*30)
print(driver.get_cookie("PSTM"))