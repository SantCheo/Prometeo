# Manejo de errores al pedir un número positivo
numero = -1

while numero < 0:
  try:
      numero = int(input("Escribe un número positivo: "))
      if numero < 0:
          print("El número debe ser positivo. Intenta otra vez.")
  except ValueError:
      print("Lo que introduces debe ser un número válido.")

print(f"El número que has introducido es {numero}")