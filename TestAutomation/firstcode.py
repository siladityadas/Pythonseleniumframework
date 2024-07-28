from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
#="/Users/siladitya/Downloads/chromedriver-mac-arm64/chromedriver")
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//input[contains(@aria-label ,'username')]").send_keys("coolchintu.92@gmail.com")
time.sleep(4)
#frameObj = driver.find_element(By.XPATH,"//iframe[@id='backgroundImage']")
#driver.switch_to.frame(frameObj)
driver.execute_script("document.querySelector('body > ntp-app').shadowRoot.querySelector('#realbox').shadowRoot.querySelector('#input')")
