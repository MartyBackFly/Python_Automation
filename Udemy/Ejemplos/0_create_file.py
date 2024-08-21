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

# Obtener el directorio del script actual
directorio = os.path.dirname(__file__)

indice_siguiente = obtener_indice_siguiente(directorio)

nuevo_archivo = generar_nombre_unico(directorio, indice_siguiente)
with open(os.path.join(directorio, nuevo_archivo), 'w') as archivo:
    archivo.write("from aafuncionimprimir import espacio as aa \nfrom aafuncionimprimir import rayita as zz \nfrom aafuncionimprimir import espacio_numero as az")

print(f"Se ha creado el archivo {nuevo_archivo} con éxito.")
