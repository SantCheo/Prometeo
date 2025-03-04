# numeros = [1,2,3]

# #Feo
# primero = numeros [0]
# segundo = numeros [1]
# tercero = numeros [2]

# print (primero, segundo, tercero)

# primero, segundo, tercero = numeros
# print (primero)
numeros = [1,2,3,4,5,6,7,8,9]
primero, segundo, *otros, penultimo, ultimo= numeros
print (primero, otros)
print (primero, segundo, otros)
print (segundo, penultimo)
print (ultimo)