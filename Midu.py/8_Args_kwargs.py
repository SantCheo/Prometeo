# Argumentos de longitud variable (*args)
# La siguiente función sumar_numeros utiliza *args para sumar todos los números que se le pasan como argumentos:

# Ejemplo: Uso de *args para sumar números

# # Argumentos de longitud de variable (*args)
# def sumar_numeros(*args):
#   suma = 0
#   for numero in args:
#       suma += numero
#   return suma

# print(sumar_numeros(1, 2, 3, 4, 5))
# print(sumar_numeros(1, 2))
# print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# Argumentos de clave-valor variable (**kwargs)
# La siguiente función mostrar_informacion_de utiliza **kwargs para recibir un número variable de argumentos nombrados y mostrarlos:

# Ejemplo: Uso de **kwargs para mostrar información

# # Argumentos de clave-valor variable (**kwargs)
# def mostrar_informacion_de(**kwargs):
#   for clave, valor in kwargs.items():
#       print(f"{clave}: {valor}")

# mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
# print("\n")
# mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
# print("\n")
# mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
# print("\n")
# mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)