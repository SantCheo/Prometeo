#Ejercicio1
#Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje “secreto”.

# mensaje = ["C", "o","d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# secreto = mensaje [7:]
# print (secreto)

#Ejercicio 2
#Intercambia la primera y la última posición utilizando solo asignación por índice.
# ##numeros[0], numeros[-1] = numeros[-1], numeros[0]
# numeros = [10, 20, 30, 40, 50]
# numeros[0]=50
# numeros[-1]= 10
# print (numeros)

#Ejercicio 3
#Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# sandwich= pan + ingredientes + pan_abajo
# print (sandwich)

#EJERCICIO 4 
# Crea una nueva lista que contenga los elementos de la lista original duplicados. 
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
# lista = [1, 2, 3]
# lista2= lista * 2
# print (lista2)

# Ejercicio 5: Extrayendo el centro

#Dada una lista con un número impar de elementos, extrae el elemento que se encuentra
#en el centro de la lista utilizando slicing. 
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30.
# lista = [10, 20, 30, 40, 50]
# print (lista [2])
# centro = len(lista) // 2
# print(lista[centro])

#Ejercicio 6: Reversa parcial
#Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
#  Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6].

lista = [1, 2, 3, 4, 5, 6]
resultado = lista [::-4]

print("\nEjercicio 6:")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)