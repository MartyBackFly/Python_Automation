# import os

# def obtener_indice_siguiente(directorio):
#     archivos = os.listdir(directorio)
#     archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]
#     indices = []
#     for archivo in archivos:
#         partes = archivo.split('_')
#         #if len(partes) == 2 and archivo.endswith('.py'):
#         try:
#                 indice = int(partes[0])
#                 indices.append(indice)
#         except ValueError:
#                 pass
#     return max(indices) + 1 if indices else 1

# directorio = 'C:/Users/fedeh/Desktop/Pytho Automation/Udemy/Selenium Testing Framework con Python/src/test'
# indice_siguiente = obtener_indice_siguiente(directorio)

# nuevo_archivo = f"test_{indice_siguiente}.py"
# with open(os.path.join(directorio, nuevo_archivo), 'w') as archivo:
#     archivo.write("from aafuncionimprimir import espacio as aa \nfrom aafuncionimprimir import rayita as zz \nfrom aafuncionimprimir import espacio_numero as az")



# print(f"Se ha creado el archivo {nuevo_archivo} con éxito.")


import os

def obtener_indice_siguiente(directorio):
    archivos = os.listdir(directorio)
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]
    indices = []
    for archivo in archivos:
        partes = archivo.split('_')
        if len(partes) > 2 and partes[1].isdigit():
            try:
                indice = int(partes[1])
                indices.append(indice)
            except ValueError:
                pass
    return max(indices) + 1 if indices else 1

def generar_nombre_unico(directorio, indice):
    while True:
        nuevo_archivo = f"test_{indice}_n.py"  # Puedes cambiar "nuevo" por el sufijo que desees
        if not os.path.exists(os.path.join(directorio, nuevo_archivo)):
            return nuevo_archivo
        indice += 1

# completo - directorio = 'C:/Users/fedeh/Desktop/Pytho Automation/Udemy/Selenium Testing Framework con Python/src/test'
directorio = 'Selenium Testing Framework con Python/src/test'
indice_siguiente = obtener_indice_siguiente(directorio)

nuevo_archivo = generar_nombre_unico(directorio, indice_siguiente)
with open(os.path.join(directorio, nuevo_archivo), 'w') as archivo:
    archivo.write("from aafuncionimprimir import espacio as aa \nfrom aafuncionimprimir import rayita as zz \nfrom aafuncionimprimir import espacio_numero as az")

print(f"Se ha creado el archivo {nuevo_archivo} con éxito.")





"""

vamos a desglosar y explicar el código línea por línea para que entiendas cómo funciona cada parte.

Importar la biblioteca os
  
   ---

   import os
os: Es una biblioteca estándar de Python que proporciona funciones para interactuar con el sistema operativo, como navegar por directorios, manipular archivos, etc.
Definir la función obtener_indice_siguiente
   
   ---
def obtener_indice_siguiente(directorio):
Esta función tiene como objetivo encontrar el próximo número de índice disponible en los archivos de un directorio específico.
Listar archivos en el directorio
   
   ---
    archivos = os.listdir(directorio)
os.listdir(directorio): Obtiene una lista de los nombres de todos los archivos y subdirectorios en el directorio especificado.
Filtrar solo archivos
   
   ---
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]
Este list comprehension filtra la lista para incluir solo los archivos (no directorios) en la lista archivos.
Inicializar lista para los índices
   
   ---
    indices = []
Se crea una lista vacía indices donde se almacenarán los números extraídos de los nombres de los archivos.
Iterar sobre los archivos y extraer el índice
python
   ---
    for archivo in archivos:
        partes = archivo.split('_')
        if len(partes) > 2 and partes[1].isdigit():
            try:
                indice = int(partes[1])
                indices.append(indice)
            except ValueError:
                pass
archivo.split('_'): Divide el nombre del archivo en partes usando el guion bajo (_) como separador. El resultado es una lista partes.
if len(partes) > 2 and partes[1].isdigit():: Esta condición verifica si el nombre del archivo tiene al menos tres partes (antes, después del primer guion bajo y después del segundo) y si la segunda parte es un número.
try: ... except ValueError:: Si la conversión de partes[1] a un número entero (int) tiene éxito, el número se agrega a la lista indices. Si falla (no es un número), se ignora el error.
Determinar el siguiente índice disponible



   ---
    return max(indices) + 1 if indices else 1
max(indices) + 1: Encuentra el número máximo en la lista indices y le suma 1 para obtener el siguiente índice disponible.
if indices else 1: Si no hay índices (es decir, si indices está vacío), el siguiente índice será 1.
Definir la función generar_nombre_unico



   ---
def generar_nombre_unico(directorio, indice):
Esta función genera un nombre de archivo único basado en el índice dado y verifica si ya existe en el directorio.
Bucle para encontrar un nombre único



   ---
    while True:
        nuevo_archivo = f"test_{indice}_nuevo.py"
        if not os.path.exists(os.path.join(directorio, nuevo_archivo)):
            return nuevo_archivo
        indice += 1
while True:: Inicia un bucle infinito hasta que se encuentra un nombre de archivo que no exista.
f"test_{indice}_nuevo.py": Genera un nombre de archivo usando el índice actual.
os.path.exists(os.path.join(directorio, nuevo_archivo)): Verifica si el archivo ya existe en el directorio.
return nuevo_archivo: Si el archivo no existe, lo retorna como nombre disponible.
indice += 1: Si el archivo existe, incrementa el índice y vuelve a intentarlo.
Usar las funciones para crear un archivo nuevo



   ---
directorio = 'C:/Users/fedeh/Desktop/Pytho Automation/Udemy/Selenium Testing Framework con Python/src/test'
indice_siguiente = obtener_indice_siguiente(directorio)

nuevo_archivo = generar_nombre_unico(directorio, indice_siguiente)
directorio = '...': Define el directorio en el que se buscarán los archivos y se creará el nuevo.
indice_siguiente = obtener_indice_siguiente(directorio): Llama a obtener_indice_siguiente para obtener el siguiente índice disponible.
nuevo_archivo = generar_nombre_unico(directorio, indice_siguiente): Llama a generar_nombre_unico para generar un nombre de archivo único basado en el índice obtenido.
Crear y escribir en el nuevo archivo



   ---
with open(os.path.join(directorio, nuevo_archivo), 'w') as archivo:
    archivo.write("from aafuncionimprimir import espacio as aa \nfrom aafuncionimprimir import rayita as zz \nfrom aafuncionimprimir import espacio_numero as az")
with open(os.path.join(directorio, nuevo_archivo), 'w') as archivo:: Abre el archivo en modo de escritura ('w'). Si el archivo no existe, lo crea; si existe, lo sobrescribe.
archivo.write("..."): Escribe el contenido especificado en el archivo.
Imprimir mensaje de éxito



   ---
print(f"Se ha creado el archivo {nuevo_archivo} con éxito.")
print(f"Se ha creado el archivo {nuevo_archivo} con éxito."): Imprime un mensaje confirmando que el archivo se creó correctamente. """