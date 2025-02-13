from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
#="/Users/siladitya/Downloads/chromedriver-mac-arm64/chromedriver")
driver.get("https://www.instagram.com/")
driver.maximize_window()

def forExplicitWaitXpath(locpath):
    wait = WebDriverWait(driver, 200)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locpath)))


forExplicitWaitXpath("//input[contains(@aria-label ,'username')]")
driver.find_element(By.XPATH,"//input[contains(@aria-label ,'username')]").send_keys("siladitya.das105@gmail.com")
forExplicitWaitXpath("//input[contains(@aria-label ,'Password')]")
driver.find_element(By.XPATH,"//input[contains(@aria-label ,'Password')]").send_keys("Sila@1992")

driver.find_element(By.XPATH,"//div[contains(text(),'Log in')]").click()
time.sleep(20)

#forExplicitWaitXpath("//button[text() = 'Save info']")
forExplicitWaitXpath("//div/div[text() = 'Not now']")
driver.find_element(By.XPATH,"//div/div[text() = 'Not now']").click()

#frameObj = driver.find_element(By.XPATH,"//iframe[@id='backgroundImage']")
#driver.switch_to.frame(frameObj)