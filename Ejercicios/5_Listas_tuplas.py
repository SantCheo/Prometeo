#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
#_____________________________________________________________________
import os
os.system ("clear")

# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.

subjects = ["Matemática", "Física", "Química", "Historia", "lengua"]
print (subjects)


# #_____________________________________________________________________
# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.

# subjects = ["Matemática", "Física", "Química", "Historia", "lengua"]

# for i in subjects:
#     print (f"Yo estudio {i}")

# #_____________________________________________________________________

# Ejercicio 3

# Escribir un programa que almacene las asignaturas de un curso 
# por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una des las asignaturas
# de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


subjects = ["Matemática", "Física", "Química", "Historia", "lengua"]

notas = []
for x in subjects:
    nota = input (f"Nota en {x}:")
    notas.append(nota)

for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + notas[i])

for i, subject in enumerate(subjects):
    print("En " + subject + " has sacado " + notas[i])