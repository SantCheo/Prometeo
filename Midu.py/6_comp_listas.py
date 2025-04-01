# La comprensión de listas (list comprehension) es una forma concisa y eficiente de crear listas en Python.
# Nos permite generar una nueva lista aplicando una expresión a cada elemento de un iterable.

# Transformar elementos con comprensión de listas
# En el siguiente ejemplo, convertimos los nombres de animales en mayúsculas de forma compacta:

# Ejemplo: Transformar elementos con list comprehension

# Usando list comprehension para convertir a mayúsculas
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]

print(animales_mayus)

# ¿Cómo funciona?
# [animal.upper() for animal in animales] crea una nueva lista donde cada animal de la lista original se convierte a mayúsculas con .upper().
# Es una alternativa más compacta a usar un bucle for tradicional.
