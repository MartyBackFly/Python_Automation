import re 
import datetime

text = "a ricardo le gusta la empanada de tu hermana "

matching  = re.findall ("empanada" , text , re.IGNORECASE)

print (matching[0])

print("-------------------------------------------------------------")

text1 = "a ricardo le gusta la empanada de tu hermana "

matching  = re.findall ("empanada|hermana " , text1, re.IGNORECASE)

print (matching)
print (matching[1])
print (matching[0])

print("-------------------------------------------------------------")

text2 = "a ricardo le gusta la empanada de tu hermana empanada en empanada"

matching  = re.findall ("empanada|hermana " , text2, re.IGNORECASE)

for results in matching :
    print(results)

print("-------------------------------------------------------------")


text3 = "a ricardo le gusta la empanada de tu Hermana Empanada en EMPANADA"

matching  = re.findall ("empanada|hermana " , text3, re.IGNORECASE)

for results in matching :
    print(results)



print("-------------------------------------------------------------")


# SIN re.ingnorecase 

text4 = "a ricardo le gusta la empanada de tu Hermana Empanada en EMPANADA"

matching  = re.findall ("empanada|hermana " , text4, )

for results in matching :
    print(results)



