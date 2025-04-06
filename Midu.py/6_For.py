#Iterar con enumerate()
# Usando enumerate para obtener índice y valor
frutas = ["manzana", "pera", "mandarina"]

for idx, value in enumerate(frutas):
  print(f"El índice es {idx} y la fruta es {value}")

  
# Conclusión
# enumerate(iterable) devuelve un índice junto con cada elemento del iterable.
# Se puede desestructurar con for idx, value in enumerate(iterable): para acceder a ambos valores fácilmente.
# Es muy útil cuando se necesita conocer la posición de los elementos mientras se itera.

# Convertir range() en una lista
# También podemos convertir un range() en una lista usando list(range(n)).
# Esto nos permite almacenar los valores en una lista y trabajar con ellos después:

# Ejemplo: Convertir range() en una lista

# # Convertir range() en una lista
nums = range(10)
list_of_nums = list(nums)

print(list_of_nums)
# ¿Cómo funciona?
# range(10) genera una secuencia de números del 0 al 9.
# list(range(10)) convierte esa secuencia en una lista de Python.