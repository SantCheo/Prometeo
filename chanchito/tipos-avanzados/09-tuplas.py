#TUPLAS
# No se pueden usar los metodos appand y pop
numeros = (1,2,3) 
numeros = (1,2,3) + (4,5,6)
print (numeros)

#convertir una lista en una tupla
punto = tuple([1,2])

print (numeros[:5])


#Desempaquetar tuplas
primero, segundo, *otros = numeros
print (primero, segundo, otros)

#Iterar tuplas
for n in numeros:
    print (n)