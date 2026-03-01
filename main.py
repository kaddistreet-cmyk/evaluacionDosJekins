from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)



#PASO 1
driver.get("https://webdriveruniversity.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "login-portal"))
)
boton_login = driver.find_element(By.ID, "login-portal")
boton_login.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 1
)
driver.switch_to.window(driver.window_handles[1])

combinaciones = [
    ("usuario1", "clave1"),
    ("usuario2", "clave2"),
    ("usuario3", "clave3")
]

for usuario, clave in combinaciones:

    try:
        alerta = driver.switch_to.alert
        alerta.accept()
    except:
        pass

driver.get("https://webdriveruniversity.com/Login-Portal/index.html")

WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//input[@placeholder="Username"]'))
    )

username_input = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
username_input.clear()
username_input.send_keys(usuario)

password_input = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
password_input.clear()
password_input.send_keys(clave)

boton_login = driver.find_element(By.ID, "login-button")
boton_login.click()

alerta = WebDriverWait(driver, 10).until(EC.alert_is_present())
alerta.accept()




#PUNTO 2
driver.switch_to.window(driver.window_handles[0])
driver.get("https://webdriveruniversity.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "to-do-list"))
)

boton_todo = driver.find_element(By.ID, "to-do-list")
boton_todo.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 2
)

driver.switch_to.window(driver.window_handles[2])

driver.get("https://webdriveruniversity.com/To-Do-List/index.html")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text"]'))
)

input_tarea = driver.find_element(By.XPATH, '//input[@type="text"]')
input_tarea.send_keys("Nueva tarea automatizada")
input_tarea.send_keys(u'\ue007')  

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//li[contains(text(),"Nueva tarea automatizada")]'))
)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//li[contains(text(),"Practice magic")]'))
)
tarea_tachar = driver.find_element(By.XPATH, '//li[contains(text(),"Practice magic")]')
tarea_tachar.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//li[contains(text(),"Go to potion class")]'))
)

boton_eliminar = driver.find_element(By.XPATH, '//li[contains(text(),"Go to potion class")]//i[@class="fa fa-trash"]')
boton_eliminar.click()



#PASO 3
driver.switch_to.window(driver.window_handles[0])
driver.get("https://webdriveruniversity.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "dropdown-checkboxes-radiobuttons"))
)
boton_dropdown = driver.find_element(By.ID, "dropdown-checkboxes-radiobuttons")
boton_dropdown.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 3
)

driver.switch_to.window(driver.window_handles[3])

driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "dropdowm-menu-1"))
)

dropdown1 = Select(driver.find_element(By.ID, "dropdowm-menu-1"))
dropdown1.select_by_visible_text("Python")

dropdown2 = Select(driver.find_element(By.ID, "dropdowm-menu-2"))
dropdown2.select_by_visible_text("JUnit")

dropdown3 = Select(driver.find_element(By.ID, "dropdowm-menu-3"))
dropdown3.select_by_visible_text("JavaScript")


#PUNTO 4
driver.switch_to.window(driver.window_handles[0])
driver.get("https://webdriveruniversity.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "iframe"))
)

boton_frame = driver.find_element(By.ID, "iframe")
boton_frame.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 4
)
driver.switch_to.window(driver.window_handles[4])

driver.get("https://webdriveruniversity.com/IFrame/index.html")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "frame"))
)

iframe = driver.find_element(By.ID, "frame")
driver.switch_to.frame(iframe)

try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
    )
    iframe_interno = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe_interno)
except:
    pass

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[contains(text(),"Our Products")]'))
)

boton_products = driver.find_element(By.XPATH, '//*[contains(text(),"Our Products")]')
boton_products.click()

driver.switch_to.default_content()

driver.switch_to.window(driver.window_handles[0])
driver.get("https://webdriveruniversity.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "popup-alerts"))
)

boton_popup = driver.find_element(By.ID, "popup-alerts")
boton_popup.click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 5
)

driver.switch_to.window(driver.window_handles[5])

driver.get("https://webdriveruniversity.com/Popup-Alerts/index.html")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "button1"))
)
boton_alert = driver.find_element(By.ID, "button1")
boton_alert.click()

alerta = WebDriverWait(driver, 10).until(EC.alert_is_present())
alerta.accept()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "button4"))
)
boton_confirm = driver.find_element(By.ID, "button4")
boton_confirm.click()

confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
confirm.accept()                       

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "confirm-alert-text"))
)
texto_confirm = driver.find_element(By.ID, "confirm-alert-text").text

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "button2"))
)
boton_modal = driver.find_element(By.ID, "button2")
boton_modal.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "myModal"))
)

titulo_modal = driver.find_element(By.CLASS_NAME, "modal-title").text
cuerpo_modal = driver.find_element(By.CLASS_NAME, "modal-body").text

boton_close = driver.find_element(By.XPATH, '//button[contains(text(),"Close")]')
boton_close.click()
