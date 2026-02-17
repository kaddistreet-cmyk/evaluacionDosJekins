from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://www.saucedemo.com/")
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//input[@placeholder="Username"]'))
)

username_input = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
username_input.send_keys("standard_user")

password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
password_input.send_keys("secret_sauce")

boton_login = driver.find_element(By.XPATH, '//input[contains(@value, "Login")]')
boton_login.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH,'//div[contains(text(), "T-Shirt")]/../../..//button[contains(text(), "Add")]')))

boton_agregar = driver.find_element(By.XPATH,'//div[contains(text(), "T-Shirt")]/../../..//button[contains(text(), "Add")]')
boton_agregar.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH,'//div[contains(text(), "Onesie")]/../../..//button[contains(text(), "Add")]')))

boton_agregar = driver.find_element(By.XPATH,'//div[contains(text(), "Onesie")]/../../..//button[contains(text(), "Add")]')
boton_agregar.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH,'//div[contains(text(), "Fleece Jacket")]/../../..//button[contains(text(), "Add")]')))

boton_agregar = driver.find_element(By.XPATH,'//div[contains(text(), "Fleece Jacket")]/../../..//button[contains(text(), "Add")]')
boton_agregar.click()

boton_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
boton_cart.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
)

boton_checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
boton_checkout.click()

time.sleep(5)
