import re 
import datetime
print("-----------------------------1--------------------------------")


text = "a ricardo le gusta salir a correr con el perro  "

search  = re.search ("empanada" , text , re.IGNORECASE)

print (search)

print("----------------------------2---------------------------------")

text1 = "a ricardo le gusta salir a correr con el perro  "

search  = re.search ("empanada" , text1, re.IGNORECASE)

if search:
    print(f"se encontro el valor ---->  {search}")
    
    # Para imprimir solo el texto coincidente
    print(f"se encontro el valor ---->  {search.group()}")
    

     # Para imprimir el span (posición)
    print(f"se encontro el valor ---->  {search.span()}")
else : 
    print ("no se encontro nada manito") 



print("----------------------------3---------------------------------")

# pongo la palabra a buscar en una variable para luego remplazar si no la encontre en el ELSE

text2 = "a ricardo le gusta salir a correr con el perro y la empanada Empanada"
pattern = "alberto"


search  = re.search (pattern, text2, re.IGNORECASE)

if search:
    print(f"se encontro el valor ---->  {search}")
    
    # Para imprimir solo el texto coincidente
    print(f"se encontro el valor ---->  {search.group()}")
    

     # Para imprimir el span (posición)
    print(f"se encontro el valor ---->  {search.span()}")
else : 
    
    print(f"No se encontró nada relacionado con: {pattern}")

print("-----------------------------4--------------------------------")




text3 = "a ricardo le gusta salir a correr con el perro y la Empanada "

search  = re.search ("empanada " , text3, re.IGNORECASE)

# espacio de caracterres hasta encontrar la palabra clave 
print(search.start())



print("--------------------------5----------------------------------")


# SIN re.ingnorecase 

text4 = "a ricardo le gusta salir a correr con el perro y la Empanada"

search  = re.search ("asdasd " , text4, )


print(search)




print("----------------------------6---------------------------------")


text5 = "a ricardo le gusta salir a correr con el perro  y a ramon el jamon y queso "
pattern = "alberto"
remplazo = "el tipo raro"


search  = re.search (pattern, text5, re.IGNORECASE)

if search:
    print(f"se encontro el valor en texto 5 ---->  {search}")
    
    # Para imprimir solo el texto coincidente
    print(f"se encontro el valor ---->  {search.group()}")
    

     # Para imprimir el span (posición)
    print(f"se encontro el valor ---->  {search.span()}")
    print(text5)
    text5 = re.sub(pattern, remplazo, text5, flags=re.IGNORECASE)
    
    
    print(text5)
   


else : 
    
    print(f"No se encontró nada relacionado con: {pattern}")




print("----------------------------7---------------------------------")

# dividir texto sobre palabra hermana 

text6 = "a ricardo le gusta salir a correr con el perro  y a ramon el jamon y queso "

split  = re.split ("hermana " , text6, re.IGNORECASE)


print(split)



print("--------------------------8-----------------------------------")


# dividir texto entre los espacios ""

text7 = "a ricardo le gusta salir a correr con el perro  y a ramon el jamon y queso "

split = re.split (" " , text7)


print(split)
print(split[1])
print(split[5])
print(split[11])
print(split[14])



print("------------------------------9-------------------------------")


# dividir texto entre los espacios ""

text8 = "a ricardo le gusta salir a correr con el perro  y a ramon el jamon y queso "

split = re.split (" " , text8)


for results in split:
    print (results)
    
print("-------------------------------------------")
if results == "petinato":
        print("son todos unos hdp")


print("------------------------------10-------------------------------")

Diccionario = {}

text9 = "este texto tiene un valor ID: 4500 texto despues de id"

# Patrón para buscar cualquier texto después de "ID:"
patron_busqueda = r"(?<=ID:\s).*"

# Patrón para buscar cualquier número después de "ID:"
patron_busqueda1 = r"(?<=ID:)\s*\d+"

# (?<=ID:): Busca cualquier coincidencia que esté precedida por "ID:".
# \s*: Permite opcionalmente espacios en blanco después de "ID:".
# \d+: Busca una o más cifras (números).




Variable = re.findall(patron_busqueda, text9 , re.IGNORECASE)
print(Variable)

Variable1 = re.findall(patron_busqueda1, text9 , re.IGNORECASE)
print(Variable1)

Diccionario["numeros"] = Variable1[0]

print(f"se almaceno el numero -->{Diccionario['numeros']} ")

print("------------------------------11-------------------------------")

text10= " Este texto contiene el valor del Scenario:HOY ahora luego despues ahora HOY de nuevo "


patron_busqueda2 = r"HOY"

remplazo = re.findall(patron_busqueda2, text10, re.IGNORECASE)
print(remplazo)

for palabra in remplazo:
     if palabra == "HOY":
          dateToday = str(datetime.date.today().strftime("%d-%m-%Y"))
          text10 = re.sub(patron_busqueda2 , dateToday, text10 , re.IGNORECASE)
          continue

print(text10)



print("------------------------------12-------------------------------")




