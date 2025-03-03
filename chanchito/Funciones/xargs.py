# def suma (a,b):
#     print(a+b)

# suma(2,5)

#Usar multiples argumentos dentro de la función
#  
def suma (*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print (resultado)
         

suma(2,5)
suma (2,3,4)
suma(2,8,7,45,32)