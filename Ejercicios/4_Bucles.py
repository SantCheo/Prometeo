# https://aprendeconalf.es/docencia/python/ejercicios/bucles/


import os
os.system ("clear")
#_____________________________________________________________________

# Ejercicio 1

# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# word = input ("ingresa una palabra: ")

# for i in range (10):
#     print (word)

#_____________________________________________________________________

# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por 
# pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# age = int (input("Ingresa edad: "))
# for i in range(age): 
#     print (i+1)

#_____________________________________________________________________

# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# n = int (input ("Ingrese un numero entero positivo:  "))

# for i in range (1, n +1):
#    if i % 2 != 0:
#     print (f"{i}", end =",")

#_____________________________________________________________________

# Ejercicio 4

# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# n = int (input ("Ingrese un numero entero positivo:  "))

# for i in range (n, -1, -1):
#     print (f"{i}", end =",")


#_____________________________________________________________________

# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# inversion = float (input ("Cantidad a invertir: ?"))
# interes= float (input ("interes anual: ?"))
# tiempo= int (input ("años de inversión: ?"))

# for i in range (1, tiempo +1):
#     compuesto = inversion * ((1 + interes)**i)
#     print (f" Capital obtenido en el año {i} es de {compuesto:.2f}")


#_____________________________________________________________________
# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

# n = int (input ("introduce un numero entero: "))

# for i in range (1, n +1):
#     print ("*"*i)


#_____________________________________________________________________
# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# for i in range (1, 10+1):
#     print ("____________________________")
#     for j in range (1,10+1):
#         print (f"{i} x {j} = {i*j}", end='\t')

#_____________________________________________________________________
# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

# n = int (input("Ingrese un numero entero: "))

# for i in range (1, n+1, 2): 
#     for j in range (i, 0, -2): 
#         print (j, end=" ")
#     print ("")


# filas = int(input("Introduce un número entero (número de filas): "))

# # Generamos el triángulo
# for i in range(1, filas + 1):
#     # El número más alto de cada fila es (2*i - 1), siempre impar
#     for j in range(2*i - 1, 0, -2):  # De mayor a menor, saltando de 2 en 2
#         print(j, end=" ")
#     print()  # Salto de línea después de cada fila
               
               
#_____________________________________________________________________
# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# password = input ("introduce contraseña: ")
# key = "chupacabra"

# while password != key:
#     print ("Error")
#     password = input ("introduce contraseña: ")
    
# print ("contraseña correcta")

#_____________________________________________________________________

# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

#n = int (input("Introduce un numero entero: "))
# i = 2
# while n % i != 0:
#     i += 1
# if n == i:
#     print ("Es un numero primo")
# else:
#     print ("No es un numero primo")

# numero = int(input("Introduce un número entero: "))

# Verificamos si el número es primo
# if numero < 2:
#     print("No es un número primo.")
# else:
#     es_primo = True
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             es_primo = False
#             break
#     if es_primo:
#         print(f"{numero} es un número primo.")
#     else:
#         print(f"{numero} no es un número primo.")

#_____________________________________________________________________

# Ejercicio 11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última.

# word = input ("introduce una palabra: ")

# palabra= word[::-1]
# for x in range (len(world)-1, -1,-1):
#     print (world[x])



# for letter in word[::-1]:
#     print(letter)

# for letter in reversed(word):
#     print(letter)


#_____________________________________________________________________
# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

# word = input ("Ingrese una palabra: ")
# letter = input ("Ingresa una letra: ")

# contador = 0
# for i in word:
#     if letter == i:
#         contador+= 1

# print (f" la letra '{letter}' está en '{word}': {contador} veces")

# print (f"{word.lower().count(letter.lower())}")

 #_____________________________________________________________________      
# Ejercicio 13

# Escribir un programa que muestre el eco de todo lo que el 
# usuario introduzca hasta que el usuario escriba “salir” que terminará.      



# while True:
#     word= input ("Hola: ")
#     if word == "salir":
#         break
#     print (word)

