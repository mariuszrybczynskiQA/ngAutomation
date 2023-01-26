from selenium.webdriver.support import expected_conditions as EC

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

username = "TestUsername1"
password = "testpassword1"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://albiononline.com/en/home")
driver.find_element(By.CSS_SELECTOR, "li.meta-nav__item:nth-child(2) > a:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "#login_submit")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/nav/div[2]/div[2]/div/div[1]/a/span[1]').is_displayed()
print("TEST PASSED")
driver.quit()





