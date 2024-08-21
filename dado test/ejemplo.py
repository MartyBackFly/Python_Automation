
# pip install selenium



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador (en este caso, Chrome)
driver = webdriver.Chrome()

# Navegar a una URL específica
driver.get("https://www.ejemplo.com")

# Esperar un tiempo (en segundos) para que la página cargue completamente
time.sleep(2)

# Encontrar un elemento por su ID y realizar una acción (en este caso, ingresar texto en un campo de entrada)
elemento_texto = driver.find_element_by_id("nombre_de_elemento")
elemento_texto.send_keys("Texto de prueba")

# Encontrar un elemento por su clase y hacer clic en él
elemento_boton = driver.find_element_by_class_name("nombre_de_clase")
elemento_boton.click()

# Esperar un tiempo para que la página responda después de hacer clic
time.sleep(2)

# Puedes seguir realizando más acciones de esta manera

# Cerrar el navegador al finalizar
driver.quit()
