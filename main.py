from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://webdriveruniversity.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "ajax-loader"))
)

boton_loader = driver.find_element(By.ID, "ajax-loader")
boton_loader.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) == 2
)

driver.switch_to.window(driver.window_handles[1])

WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.ID, "button1"))
)

boton = driver.find_element(By.ID, "button1")
boton.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Close']"))
)

driver.find_element(By.XPATH, "//button[text()='Close']").click()
