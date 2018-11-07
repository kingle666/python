from selenium import webdriver

driver_path = r"D:\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
submituBtm = driver.find_element_by_id('su')
print(type(submituBtm))
print(submituBtm.get_attribute("value"))
driver.save_screenshot('baidu.jpg')