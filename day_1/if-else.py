l = list ()
texto= input ('Introduce un numero entero: ')
if texto.isnumeric():
    num = int (texto)
    l.append(num)
    print("Número "+ str (num)+  " añadido a la lista")
else: 
    print ("No has introducido un número entero")
ejemp106.1. py
list()
1
input ( Introduce
texto
if texto.isnumeric()
num = int(texto)
1. append(num)
print("Número " +
else:
print("No has introducido un
#Creamos una lista vacia
un número
entero por teclado:
# Comprobamos si son numeros
str(num) + '
añadido a la lista")
número entero")
ejemp106.2. py
= { "56862634" :
d
, "43394932" :
37
32}
#Creamos diccionario
texto = input("lntroduce un documento de indentidad ")
if texto in d.
#Comprobamos si esta en el diccionario
print("La edad de " +
str(d [texto] ) )
texto
e Ise:
input("Documento no existente. Introduce edad:
edad
if edad.isnumeric()
8
print(d)
num = int(edad)
d [texto]
print("Añadido a1 diccionario")
#Mostramos por pantalla el diccionario

