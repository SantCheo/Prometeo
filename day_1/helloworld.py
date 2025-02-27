# leg_a = float(input("Ingresa la longitud del primer cateto: "))
# leg_b = float(input("Ingresa la longitud del segundo cateto: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("La longitud de la hipotenusa es:", hypo)



# hour = int(input("Hora de inicio (horas): "))
# mins = int(input("Minuto de inicio (minutos): "))
# dura = int(input("Duración del evento (minutos) "))
# # encuentra el número total de minutos
# # encuentra el número de horas ocultas en los minutos y actualiza las horas
# # corrige los minutos para que estén en un rango de (0..59)1
# # corrige las horas para que estén en un rango de (0..23) 
# print(hour, ":", mins, sep='')

# Se leen dos números

# plant= input('..')

# if plant=='Espatifilo':
#     print ('Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!')
    
# elif plant== 'pelargonio':
#     print ('¡Espatifilo!, ¡No pelargonio!')
    
# else :                                                                                                                                                                                                  
#     print ('No, ¡quiero un gran Espatifilo!')                                     

# year = int(input("Introduce un año: "))

# if year < 1582:
# 	print("No esta dentro del período del calendario Gregoriano")
# else:
# 	if year % 4 != 0:
# 		print("Año Común")
# 	elif year % 100 != 0:
# 		print("Año Bisiesto")
# 	elif year % 400 != 0:
# 		print("Año Común")
# 	else:
# 		print("Año Bisiesto")


# 
#  Almacena el actual número más grande aquí.
# largest_number = -999999999
 
# Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
# while number != -1:
#     ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         Sí si, se actualiza largest_number.
#         largest_number = number
#     Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
# print("El número más grande es:", largest_number)


# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

# odd_numbers = 0
# even_numbers = 0

# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while number:
#     # Verificar si el número es impar.
#     if number % 2:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))

# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)

# secret_number = 777

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)
# numero= int ( input (' ingrese un número entero'))

# while secret_number != numero:
#             print ("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#             numero= int ( input (' ingrese un número entero'))
# print ('¡Bien hecho, muggle! Eres libre ahora.')


# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")