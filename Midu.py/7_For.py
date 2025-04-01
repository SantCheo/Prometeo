import os
os.system ("clear")
# Pon en práctica lo aprendido resolviendo los siguientes ejercicios usando bucles for.

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

# for x in range (1,21,2):
#     print (x)

#     Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números: numeros = [10, 20, 30, 40, 50] Calcula la media de los números usando un bucle for.

# numeros = [10, 20, 30, 40, 50]
# suma = 0
# for x in numeros:
#     suma+= x

# media = suma / len (numeros)
# print (f"la media de la suma de los numeros es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

# numeros = [15, 5, 25, 10, 20]
# top = 0
# for x in numeros :
#     if x > top:
#         top = x
# print (f"El número máximo es: {top}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

# [num for num in lista if num % 2 == 0] recorre cada número de la lista original.
# Solo añade a la nueva lista los números que cumplen la condición num % 2 == 0 (es decir, los pares).

# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
# print (palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# letra = input("Introduce una letra: ").lower()  # Convertimos la letra a minúscula
# contador = 0
# for palabra in palabras:
#   if palabra.lower().startswith(letra):  # Comparamos en minúsculas
#     contador += 1
# print(f"Hay {contador} palabras que empiezan con la letra {letra}")


# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().

# for x in range (1,21,2):
#     print (x)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

# for x in range(5,51,5):
#     print (x)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

# for x in range (10,0,-1):
#     print (x)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

# suma= 0
# for x in range (1,101):
#     suma+= x
# print (f"la suma de todos los numeros es: {suma}")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

numero = int (input("Introduce un numero: "))
for x in range (1,11):
    print (f"{numero}x{x}= {numero*x}")

    

