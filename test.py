from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#object of Options class
op = webdriver.ChromeOptions()
#set chromedriver.exe path
driver = webdriver.Chrome(options=op)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.seleniumhq.org/download/");
#get user Agent with execute_script
a= driver.execute_script("return navigator.userAgent")
print("User agent:")
print(a)
#close browser session
driver.quit()