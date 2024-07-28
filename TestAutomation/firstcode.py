from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
#="/Users/siladitya/Downloads/chromedriver-mac-arm64/chromedriver")
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[contains(@aria-label ,'username')]").send_keys("siladitya.das105@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//input[contains(@aria-label ,'Password')]").send_keys("JJJJ")
time.sleep(2)
driver.find_element(By.XPATH,"//div[contains(text(),'Log in')]").click()
time.sleep(10)
#frameObj = driver.find_element(By.XPATH,"//iframe[@id='backgroundImage']")
#driver.switch_to.frame(frameObj)