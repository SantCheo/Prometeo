#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/

import os
os.system ("clear")
#________________________________________________________________________________________________________________________________________________


#1 
# Escribir un programa que pregunte al usuario su edad y muestre por 
# pantalla si es mayor de edad o no.

# age =  int (input ("Indica tu edad por favor: "))

# if age >= 18:
#     print ("Eres mayor de edad")
# else:
#     print ("Eres menor de Edad")
#________________________________________________________________________________________________________________________________________________


#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# contraseña = "contraseña"

# contraseña_usuario= input ("Introduce la contraseña:") 

# if contraseña == contraseña_usuario.lower():
#     print ("contraseña correcta")

# else: 
#     print ("contraseña incorrecta")
#________________________________________________________________________________________________________________________________________________


# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por 
# pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# number1 = int (input ("Introduce un numero: "))
# number2 = int (input ("Introduce otro numero: "))

# if number2 == 0:
#     print ("Error no se puede dividir entre 0")
# else: 
#     division = number1 / number2
#     print (f"La division de {number1} entre {number2} es {division}")
#________________________________________________________________________________________________________________________________________________


# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# number = int (input ("Introduce un numero entero: "))

# if number % 2 == 0:
#     print (f"El numero {number} es par")
# else: 
#     print (f"El numero {number} es impar ")
#________________________________________________________________________________________________________________________________________________


# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
# iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad 
# y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# edad = int (input ("indica tu edad: "))
# ingresos = float (input ("Indica tus ingresos mensuales: "))

# if edad >= 16 and ingresos >= 1000:
#     print ("Debes tributar")
# else: 
#     print ("No debes tributar")
#________________________________________________________________________________________________________________________________________________


#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A esta formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo B por el resto. 
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# sex = input ("¿Cúal es tu sexo (M,H)?: ")
# name = input ("¿Cúal es tu nombre: ")

# if sex == "M" and name.lower() < "m" or sex == "H" and name.lower() > "n":
#     print ("grupo A")
# else: 
#     print ("grupo B")
#________________________________________________________________________________________________________________________________________________

#Ejercicio 7   
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# renta = float (input ("¿Cúal es tu renta anual?:  "))

# if renta < 10000:
#     pagar = renta *  0.05
#     print (f"El tipo impositivo que le corresponde es de 5% \n Paga al Estado: {pagar}")
# elif renta < 20000:
#     pagar = renta *  0.15
#     print (f"el tipo impositivo que le corresponde es de 15% \n Paga al Estado: {pagar}")
# elif renta < 35000:
#     pagar = renta *  0.2
#     print (f"el tipo impositivo que le corresponde es de 20% \n Paga al Estado: {pagar}")
# elif renta < 60000:
#     pagar = renta *  0.3
#     print (f"el tipo impositivo que le corresponde es de 30% \n Paga al Estado: {pagar}")
# else:
#     pagar = renta *  0.45
#     print (f"el tipo impositivo que le corresponde es de 45% \n Paga al Estado: {pagar}")

#________________________________________________________________________________________________________________________________________________

# # Preguntar al usuario por la renta
# renta = float(input("¿Cuál es tu renta anual? "))
# # Condicional para determinar el tipo impositivo dependiendo de la renta
# if renta < 10000:
#     tipo = 5
# elif renta < 20000:
#     tipo = 15
# elif renta < 35000:
#     tipo = 20
# elif renta < 60000:
#     tipo = 30
# else:
#     tipo = 45
# # Mostrar por pantalla el producto de la renta por el tipo impositivo
# print("Tienes que pagar ", renta * tipo / 100, "€", sep='')

#________________________________________________________________________________________________________________________________________________


# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
# pero no valores intermedios entre las cifras mencionadas. A continuación se muestra 
# una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.

# puntos = float( input("Puntuación final: "))

# if puntos == 0.0: 
#     print ("Inacepatable, sigue intentando")
# elif puntos == 0.4:
#     print (f"Aceptable su bono es de: {2400  * 0.4} ")
# elif puntos >= 0.6:
#     print (f"Meritorio su bono es de: {2400*0.6}")

# bonificacion = 2400
# inaceptable = 0
# aceptable = 0.4
# meritorio = 0.6
# puntos = float(input("Introduce tu puntuación: "))
# # Clasifiación por niveles de rendimiento
# if puntos == inaceptable:
#     nivel = "Inaceptable"
# elif puntos == aceptable:
#     nivel = "Aceptable"
# elif puntos >= 0.6:
#     nivel = "Meritorio"
# else:
#     nivel = ""
# # Mostrar nivel de rendimiento
# if nivel == "":
#     print("Esta puntuación no es válida")
# else:
#     print("Tu nivel de rendimiento es %s" % nivel)
#     print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))

#_________________________________________________________________________________________


# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

# age = int (input("Edad: "))

# if age > 18: 
#     print ("10€")
# elif age >= 4:
#     print ("5€")
# else:
#     print("Pasas gratis")
#_________________________________________________________________________________________


# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


print ("----------Bievenido a la Pizzeria Bella Napoli-----------------")

tipo =  input ("Deseas una pizza vegetariana: ")
if tipo == "si":
    a = "Pimiento"
    b = "Tofu"
    ingrediente = input ("Elije un ingrediente:\n a Pimiento\n b Tofu\n:  ")
    if ingrediente == a :
        print (f"Su pizza vegetariana, contiene los ingredientes: mozzarella, tomate y {a}")
    else:
        print (f"Su pizza vegetariana, contiene los ingredientes: mozzarella, tomate y {b}")
    
    
else:
    c = "Peperoni"
    d = "Jamón"
    e = "Salmón"
    ingrediente = input ("Elije un ingrediente:\n c Peperoni\n d Jamón\n e Salmón\n:  ") 
    if ingrediente == c: 
        print (f"Su pizza no es vegeteriana, contiene los ingredientes: mozzarella, tomate y {c}")
    elif ingrediente == d: 
        print (f"Su pizza no es vegetariana contiene los ingredientes: mozzarella, tomate y {d}")
    else:
        print (f"Su pizza no es vegetariana contiene los ingredientes: mozzarella, tomate y {e}")
