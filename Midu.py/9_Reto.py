import os
os.system ("clear")



# # def alfa (text):
# #     text = text.lower()
# #     contar_t= text.count("t")
# #     contar_j= text.count("j")
# #     print(f"count_r: {contar_t} count_j: {contar_j}")
# #     return contar_t == contar_j

# # print (alfa("vargneyjjktgulktwrh"))

# #RETO 2
# # En Jurassic Park, los dinosaurios carnívoros, como el temible T-Rex, 
# # depositan un número par de huevos. En este ejercicio, 
# # se nos proporciona una lista de números enteros que representan la 
# # cantidad de huevos puestos por diferentes dinosaurios en el parque.

# # Objetivo
# # Escribe una función en Python que reciba una lista de números enteros 
# # y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros, 
# # es decir, la suma de todos los números pares en la lista.

# # def tocar_los_huevos (egg_list) -> int:
# #     dino_car= 0
# #     eggs_car= 0
# #     for eggs in egg_list:
# #         if eggs % 2 == 0:
# #             dino_car+= 1
# #             eggs_car+= eggs
    
#     return f"Huevos:{eggs_car}, Dinosaurios carnivoros: {dino_car}"

# egg_list = [4,3,6,7,8,9,13,12,14,15,16,13]

# tocar_los_huevos (egg_list)
# print (tocar_los_huevos(egg_list))

# # Dado un array de números y un número objetivo (goal), 
# # necesitamos encontrar los dos primeros 
# # números en el array cuya suma sea igual a ese número objetivo. 
# # Si existe tal combinación, 
# # la función debe devolver los índices de estos dos números. 
# # Si no se encuentra ninguna combinación, debe devolver None.




# def find_goal(lista, goal):
#     for i in range(len(lista)):
#         for j in range(i +1, len (lista)):
#             if lista [i] + lista [j] == goal:
#                 return [i ,j]
#     print ()
#     return None


# lista = [1,2,3,4,5,6,7,8,9 ]
# goal = 13
# print (find_goal(lista, goal))

# import re

# correo = 'lo.que+sea@shopping.online'
# patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
# validacion = re.finditer(patron, correo)
# print (validacion is not None)



# # , miguel@gov.co.ok, lo.que+sea@shopping.online

# from datetime import datetime

# fecha1 = datetime.strptime("2023-05-15", "%Y-%m-%d")
# fecha2 = datetime.strptime("2023-06-15", "%Y-%m-%d")
# diferencia = fecha2 - fecha1
# print(diferencia)


texto =(" ...la función debe devolver los índices de estos dos números... " )
remplazo = texto.replace("debe", "deberia") # reemplaza la palabra "debe" por "deberia"
posicion = texto.find("debe") # busca la posicion de la palabra "debe"
xato = remplazo.split("devolver")# # separa el texto en dos partes usando "devolver" como separador
mutiplica = texto * 2 # multiplica la cadena
eliminar = texto.strip() # elimina los espacios en blanco al inicio y al final de la cadena
eliminar2 = eliminar.strip(".")
print (xato)
print (f"la posicion del texto es {posicion}")
print (mutiplica)
print (eliminar)
print (eliminar2)