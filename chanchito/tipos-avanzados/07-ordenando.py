numeros=[2,4,1,45,75,22]

# #Metodo .sort(), ordena la lista 
# numeros.sort() 
# print(numeros)  #[1, 2, 4, 22, 45, 75]

# numeros.sort(reverse=True)  # Orden descendente
# print(numeros)  #[75, 45, 22, 4, 2, 1]

#  Usar la función sorted()
#devuelve una nueva lista ordenada y no modifica
# la lista original.
# numeros2 = sorted (numeros)
# print (numeros2)

# numeros2 = sorted (numeros, reverse=True)
# print (numeros2)

# usuarios= [ 
#             [4, "Chanchito"],
#             [1, "Felipe"],
#             [5, "Pulga"]
# ]

# usuarios.sort () # Siempre y cuando los Id esten al comienzo del listado
# print (usuarios) 
#[[1, 'Felipe'], [4, 'Chanchito'], [5, 'Pulga']

usuarios= [ 
            [ "Chanchito", 4],
            [ "Felipe", 1],
            [ "Pulga", 5]
]

def ordena(elemento):
    return elemento [1]

# usuarios.sort(key=ordena, reverse=True)
# print (usuarios) 

#Funciones Lambda

usuarios.sort(key=lambda el:el[1],  reverse=True)
print (usuarios) 
