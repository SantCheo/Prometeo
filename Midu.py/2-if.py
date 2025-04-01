
import os
os.system ("clear")
#Ejercicio1
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales.
# number_1 = input ("numero 1: ")
# number_2 = input ("number 2: ")
# if number_1 > number_2:
#     print ( f"El numero: {number_1} es mayor que el numero: {number_2}")
# elif number_1 == number_2:
#     print ("Los numeros son iguales")
# else:
#     print (f"el numero: {number_2} es mayor que el numero: {number_1}")


# Ejercicio 2: Calculadora simple

# Pide al usuario dos números y una operación (+, -, *, /). Realiza la operación y muestra el resultado (maneja la división entre cero).

# num1 = float(input ("numero 1: "))
# num2 = float(input ("number 2: "))
# opera = input(" Qué operación deseas realizar ( +,-,*,/):  ")

# if opera == "+":
#     print (f"El resultado de la suma es: {num1+num2}")
# elif opera == "-":
#      print (f"El resultado de la resta es: {num1-num2}")
# elif opera == "*":
#       print (f"El resultado de la multiplicación es: {num1*num2}")
# elif opera == "/":
#       if num2 == 0:
#            print ("No se puede dividir entre cero")
#       else:
#         print (f"El resultado de la división es: {num1 / num2}")
# else: 
#      print ("operación no permitida")


# Ejercicio 3: Año bisiesto

# Pide al usuario que introduzca un año y determina si es bisiesto:

# Es divisible por 4.
# Excepto si es divisible por 100, pero no por 400.
# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print(f"{anio} es un año bisiesto.")
# else:
#     print(f"{anio} no es un año bisiesto.")


anio = int(input("Año: "))
if  anio  % 4 == 0 and anio % 100 != 0 : 
        print ("año bisiesto")
elif anio % 400 == 0:
          print ("2.año bisiesto")
else: 
        print ("no es bisiesto")


# for numero in range(1, 2001):  # Números desde 1 hasta 2000
#     if numero % 4 == 0 and numero % 100 != 0:
#         print(numero, end=" ")  # Imprimir en una sola línea

# Ejercicio 4: Categorizar edades

#Clasifica una edad ingresada por el usuario en:

# Bebé =  (0-2 años)
# Niño (3-12 años)
# Adolescente (13-17 años)
# Adulto (18-64 años)
# Adulto mayor (65 años o más)

# age = int (input ("Ingrese edad: "))

# if age >= 65:
#      print ("Adulto mayor")
# elif age >= 18:
#      print ("Adulto")
# elif age >= 13: 
#      print ("Adolecente")
# elif age >= 3:
#      print ("Niño")
# elif age >=0:
#      print ("Bebe")
# else:
#      print ("Su existencia trasiende el plano físico y espiritual")