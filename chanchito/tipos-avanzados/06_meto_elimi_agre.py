mascotas = ["Pelusa", "Wolfgang","Pulga", "Felipe","Wolfgang", "Chanchito Feliz"]

#Metodo .insert() agregar elementos a la lista 
mascotas.insert(2,"Melvin")
print(mascotas)

#Metodo .append() agregar elemento al final de la lista
mascotas.append ("Chachito triste")
print (mascotas)
#Con extend, puedes añadir múltiples elementos al final de la lista.
# Añadir varios elementos al final
lista1 = ['a', 'b', 'c', 'd']
lista1.extend(['😃', '😍'])  # Agrega varios elementos
print(lista1)  # ['a', 'b', 'c', 'd', '😃', '😍']


#Metodo .remove() eliminar elemento. elimina el primer
# elemento encontrado
mascotas.remove("Wolfgang")
print (mascotas)

#Metodo .pop() elimina el ultimo elemento de la lista
# O indicar el elemento a eliminar (..)
# tambien se puede usar del []
mascotas.pop()
mascotas.pop(0)
del mascotas [1]
print (mascotas)
 
#Metodo .clear() limpiar lista
mascotas.clear()
print(mascotas)

# Ordenar listas modificando la original
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()  # Ordena la lista original
print(numbers)  # [2, 3, 8, 10, 99, 101]

# Ordenar listas creando una nueva lista
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)  # Crea una nueva lista ordenada
print(sorted_numbers)  # [2, 3, 8, 10, 99, 101]
print(numbers)  # [3, 10, 2, 8, 99, 101] (la lista original no se modifica)


# Ordenar una lista de cadenas en minúsculas
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)  # Crea una lista ordenada alfabéticamente
print(sorted_frutas)  # ['limón', 'limón', 'manzana', 'manzana', 'pera', 'pera']

# Ordenar una lista de cadenas con mayúsculas y minúsculas
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)  # Ordena ignorando mayúsculas y minúsculas
print(frutas)  # ['Limón', 'limón', 'manzana', 'manzana', 'Pera', 'pera']

# Tamaño de la lista
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals))  # -> 4

# Contar elementos en la lista
animals = ['🐶', '🐼', '🐨', '🐶']
print(animals.count('🐶'))  # -> 2

# Verificar si un elemento está en la lista
animals = ['🐶', '🐼', '🐨', '🐶']
print('🐼' in animals)  # -> True
print('🐹' in animals)  # -> False