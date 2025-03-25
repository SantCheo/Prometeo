# print("\nEjercicio 1: Imprimir mensajes")
# print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# name  = input("¿Cual es tu nombre?: ")
# city = input ("En que ciudad vives?: ")
# print (f"Bienvenido {name}, vives en {city}")

#Ejercicio2
# print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
# print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
# a = 15
# b = 3.14159
# c = "Hola mundo"
# d = True
# e = None

# print (type(a), type(b), type(c), type(d),type(e), sep= "\n" )

#Ejercicio #3
# print("\nEjercicio 3: Casting de tipos")
# print("Convierte la cadena \"12345\" a un entero y luego a un float.")
# print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# print (type(float (int ("12345"))))
# print (int (3.99))

#Ejercicio 4
# print("\nEjercicio 4: Variables")
# print("Crea variables para tu nombre, edad y altura.")
# print("Usa f-strings para imprimir una presentación.")

# name = "Alfredo"
# age = 32
# stature = 1.73 
# print (f"Hola! Me llamo {name} y tengo {age} años, mido {stature} metros")


import os
os.system ("clear")

# print("\nEjercicio 5: Números")
# print("1. Crea una variable con el número PI (sin asignar una variable)")
# print("2. Redondea el número con round()")
# print("3. Haz la división entera entre el número que te salió y el número 2")
# print("4. El resultado debería ser 1")

# Pi = 3.14
# print (round (3.14)//2)
# print ("hola")

edad = 19
tiene_dinero = True

if  edad > 18:
    print("Puedes pasar")
elif tiene_dinero:
    print("Adelante")
else:
  print ("Quedate en casa")