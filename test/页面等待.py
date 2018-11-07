from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
drver_path = r"D:\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=drver_path)
driver.get('https://www.baidu.com/')

driver.execute_script("windows.open('https://www.douban.com/')")
# driver.implicitly_wait(20)

# WebDriverWait(driver,10).until(
#     EC.presence_of_element_located(By.ID,'sfasfsd')
# )

print(driver.current_url)