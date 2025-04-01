#https://aprendeconalf.es/docencia/python/ejercicios/cadenas/

# name = input ("Nombre de usuario: ")
# numero = int (input ("indique un numero entero: "))

# print (f"gracias.. \n {name * numero}")

#2
# lower(): Convierte todo el texto a minúsculas.
# upper(): Convierte todo el texto a mayúsculas.
# title(): Convierte la primera letra de cada palabra en mayúscula.

# nombre = input ("Ingrese sus Nombres y apellidos completos: ")

# # Mostrar el nombre en minúsculas
# print("Nombre en minúsculas:", nombre.lower())

# # Mostrar el nombre en mayúsculas
# print("Nombre en mayúsculas:", nombre.upper())

# # Mostrar el nombre con la primera letra de cada palabra en mayúscula
# print("Nombre con la primera letra en mayúscula:", nombre.title())

#3

# nombre = input ("Ingrese sus Nombres y apellidos completos: ")
# nombre = nombre.upper()
# # Eliminamos los espacios y contamos solo las letras
# #len contador 
# numero = len(nombre.replace(" ", ""))
# #texto.replace(" ", ""): Busca todos los espacios (" ") en la cadena 
# #texto y los reemplaza con una cadena vacía ("").

# print ("el nombre:", nombre.upper(), " contiene: ", numero , "letras")

#4

# prefijo= input("indica el prefijo")
# numero = input ("indique el numero")
# extension= input ("indique la extensión")

# print ("llamando...", numero)

# tel= input ("introduce el numero de telefono en formato: +xx-xxxxxxxxx-xx   ")
# print ("llanando...", tel[4:-3])

#5
# frase = input ("introduzca una frase: ")

# print (frase[::-1])

#6
# frase = input ("introduce una frase: ")
# vocal= input ("introduce una vocal: ")
# print (frase.replace(vocal, vocal.upper()))

#7

mail= input ("escribe un correo electronico: ")

