import subprocess
import tkinter as tk

# Ejecutar el comando pip list desde Python para obtener una lista de paquetes instalados
result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')

# Imprimir la salida (lista de paquetes instalados)
print(output)
