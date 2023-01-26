from telnetlib import EC

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

emailAddress = "ted334434@gmail.com"
password = "Tfs3ggg33331234"


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://albiononline.com/en/home")
driver.find_element(By.CSS_SELECTOR, "li.meta-nav__item:nth-child(1) > a:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, "#fos_user_form_email").send_keys(emailAddress)
driver.find_element(By.CSS_SELECTOR, "#fos_user_password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "#fos_user_Password_second").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "#terms_and_conditions").click()
driver.find_element(By.CSS_SELECTOR, "#accountSubmitButton").click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, ".alert-box").is_displayed()
print("TEST PASSED")
driver.quit()






