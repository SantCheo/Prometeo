# https://aprendeconalf.es/docencia/python/ejercicios/cadenas/

# name = input ("Nombre de usuario: ")
# numero = int (input ("indique un numero entero: "))

# print (f"gracias..\n {(name + '\n')* numero}")

# 2
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

# 3

# nombre = input ("Ingrese sus Nombres y apellidos completos: ")
# nombre = nombre.upper()
# # Eliminamos los espacios y contamos solo las letras
# #len contador 
# numero = len(nombre.replace(" ", ""))
# #texto.replace(" ", ""): Busca todos los espacios (" ") en la cadena 
# #texto y los reemplaza con una cadena vacía ("").

# print ("el nombre:", nombre.upper(), " contiene: ", numero , "letras")

# 4

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

# #7

# email = input("Introduce tu correo electrónico: ")
# print(email[:email.find('@')] + '@ceu.es')

# correo = input("Introduce tu correo electrónico: ")

# # Dividimos el correo en nombre y dominio
# nombre_usuario = correo.split('@')[0]

# # Creamos un nuevo correo con el dominio ceu.es
# nuevo_correo = nombre_usuario + '@ceu.es'

# print("Tu nuevo correo es:", nuevo_correo)

#8
# el metodo split solo es para string
# precio = (input("Introduce el precio con dos decimales: "))
# # valor = precio.split (".")
# # print (f"El precio del producto es {valor[0]} euros con {valor[1]} centimos")

# print (f"el precio del producto es {precio[:precio.find('.')]} euros con {precio[precio.find('.')+1:]} centimos")

#9
born = input ("introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
birthday = born.split("/")
print (f"Naciste el {birthday[0]} del {birthday [1]} del {birthday[2]}")
print (f"Tu fecha de nacimiento es : {born[:2]} del {born[3:5]} del año {born[-4:]}")

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)

#10

# compra = input ("intruduce los productos de la cesta de tu compra: ")
# # compra = compra.split (",")
# print (f"Tienes en tu carrito de compra:\n{compra.replace(',','\n')}")
# # Divide la cadena usando .split() y luego une las partes con un salto de línea
# # '\n'.join(...): Toma esa lista y une sus elementos con un salto de línea (\n). 
# # Así, cada producto aparecerá en una línea diferente.
# print('\n'.join(compra.split(',')))

#11
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
#  y muestre por pantalla una cadena con el nombre del producto 
# seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales

# Pedimos los datos del producto
producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))

# Calculamos el coste total
coste_total = precio * unidades

# Mostramos el resultado con el formato adecuado
print(f"{producto}: Precio unitario: {precio:6.2f}, Unidades: {unidades:3d}, Coste total: {coste_total:8.2f}")


# precio:6.2f: El precio unitario tiene un total de 6 caracteres, incluyendo 2 decimales. Si el número tiene menos de 6 caracteres, se rellena con espacios a la izquierda.

# unidades:3d: El número de unidades tiene 3 dígitos, y si es menor que 100, se completa con espacios a la izquierda.

# coste_total:8.2f: El coste total tiene un total de 8 caracteres, incluyendo 2 decimales. Los espacios a la izquierda se rellenan automáticamente.

