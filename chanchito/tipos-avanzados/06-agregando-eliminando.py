mascotas = ["Pelusa", "Wolfgang","Pulga", "Felipe","Wolfgang", "Chanchito Feliz"]

#Metodo .insert() agregar elementos a la lista 
mascotas.insert(2,"Melvin")
print(mascotas)

#Metodo .append() agregar elemento al final de la lista
mascotas.append ("Chachito triste")
print (mascotas)

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