import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
RadioButtn = driver.find_elements(By.CSS_SELECTOR,'.radioButton')
print(len(RadioButtn))
for rdButtn in RadioButtn:
    print(rdButtn.get_attribute("value"))


#####Select Value from dropdown
#dropDown = driver.find_element(By.CSS_SELECTOR,'#dropdown-class-example')
selectDp = Select(driver.find_element(By.CSS_SELECTOR,'#dropdown-class-example'))
print(selectDp.is_multiple)

###Alert

driver.find_element(By.CSS_SELECTOR,'#name').send_keys("Siladitya")
driver.find_element(By.CSS_SELECTOR,'#alertbtn').click()
alert = driver.switch_to.alert
print(alert.accept())
time.sleep(5)