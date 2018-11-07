from selenium import webdriver
drver_path = r"D:\driver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://222.92.112.66:8080")
driver = webdriver.Chrome(executable_path=drver_path,chrome_options=options)

driver.get("http://httpbin.org/ip")