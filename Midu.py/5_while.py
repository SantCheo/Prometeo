# import os
# os.system ("clear")

#Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

# numeros = 10
# while numeros > 0:
#     print (numeros)
#     numeros+= -1
    

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")

# numeros = 0
# suma= 0
# while numeros < 20:
#     numeros+=1
#     if numeros % 2 == 0:
#         suma+= numeros    

# print (f"La suma de los numeros pares es igual a: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# numero = int (input("introduce un numero entero positivo: "))
# factorial = numero
# while factorial > 0:
#     factorial-= 1
#     if factorial > 0:
#         numero*= factorial      
# print (numero)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")
# contador = 0
# numero = int (input ("introduce un numero: "))
# while contador < 10:
#     contador+= 1
#     print (f"{numero} * {contador} = {numero * contador} " )

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.


numero = 2
# while numero <= n:
#     if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
#         numero+= 1
#         break
     
#     print(f"{numero} es un numero primo")


print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1

