usuarios= [ 
            [ "Chanchito", 4],
            [ "Felipe", 1],
            [ "Pulga", 5]
]

# nombres= []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print (nombres)

#Transformar, map
# nombres = [usuario [0] for usuario in usuarios]
# print (nombres)

#Filtrar elementos, if usuario[1] > 2, filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print (nombres)

# #map:
# nombres = list (map(lambda usuario: usuario [0], usuarios))
# print (nombres)

# #Filter:
# menosUsuarios = list(filter(lambda usuario: usuario[1]>2, usuarios ))
# print (menosUsuarios)

lista1 = ['a', 'b', 'c', 'd']
ultimo = lista1.pop()
print(ultimo)
print(lista1)