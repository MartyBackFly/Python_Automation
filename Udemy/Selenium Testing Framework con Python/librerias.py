#######################################################
#selenium udemy 

# python.exe -m pip install --upgrade pip
import importlib
import importlib.metadata





importlib_metadata = importlib.metadata.version("importlib_metadata")
print(f"Version de importlib_metadata: {importlib_metadata}")


pillow = importlib.metadata.version("pillow")
print(f"Version de pillow: {pillow}")




pytest = importlib.metadata.version("pytest")
print(f"Version de pytest: {pytest}")

# pytest es una biblioteca de testing en Python que facilita la escritura de pruebas tanto 
# sencillas como complejas. Es ampliamente utilizada debido a su simplicidad, flexibilidad 
# y extensibilidad. A continuación se presentan algunas características clave y conceptos 
# relacionados con pytest:



Behave = importlib.metadata.version("behave")
print(f"Version de behave : {Behave}")

# behave permite escribir especificaciones de comportamiento de manera sencilla utilizando 
# el formato Gherkin. Gherkin es un lenguaje que utiliza una sintaxis muy legible que 
# describe el comportamiento esperado del software en forma de escenarios y pasos. Aquí 
# hay una descripción general de cómo funciona behave:


unittest_xml_reporting  = importlib.metadata.version("unittest_xml_reporting")
print(f"Version de unittest-xml-reporting : {unittest_xml_reporting}")

# unittest-xml-reporting es una extensión de la biblioteca unittest de Python que permite
# generar reportes de pruebas en formato XML, específicamente en el formato compatible con 
# las herramientas de integración continua como Jenkins. 


allure_pytest = importlib.metadata.version("allure_pytest")
print(f"Version de allure-pytest : {allure_pytest}")


# Allure es una herramienta de reporte para pruebas automatizadas, diseñada para generar
#  reportes visualmente atractivos y fáciles de entender a partir de los resultados 
# de las pruebas



allure_behave = importlib.metadata.version("allure_behave")
print(f"Version de allure_behave : {allure_behave}")

# Allure también se puede integrar con behave para generar reportes detallados y 
# visualmente atractivos a partir de las pruebas de comportamiento (BDD) escritas con behave. 
