import re 
import datetime

text = "a ricardo le gusta la empanada de jyq "

matching  = re.findall ("empanada" , text , re.IGNORECASE)

print (matching[0])

print("-------------------------------------------------------------")

text1 = "a ricardo le gusta la empanada de jyq "

matching  = re.findall ("empanada|jyq " , text1, re.IGNORECASE)
try:
    print (matching)
    print (matching[1])
    print (matching[0])
except:
    print("no hay coincidencias")

try:
    
    print (matching[2])
    print (matching[3])
except:
    print("no hay coincidencias 2 y 3")






print("-------------------------------------------------------------")

text2 = "a ricardo le gusta la empanada de jyq empanada en empanada"

matching  = re.findall ("empanada|jyq " , text2, re.IGNORECASE)

for results in matching :
    print(results)

print("-------------------------------------------------------------")


text3 = "a ricardo le gusta la empanada de jyq Empanada en EMPANADA"

matching  = re.findall ("empanada|hermana " , text3, re.IGNORECASE)

for results in matching :
    print(results)



print("-------------------------------------------------------------")


# SIN re.ingnorecase 

text4 = "a ricardo le gusta la empanada de jyq Empanada en EMPANADA"

matching  = re.findall ("empanada|hermana " , text4, )

for results in matching :
    print(results)



