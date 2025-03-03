# break - ejemplo

# print("La instrucción break:")
# for i in range(1,6,3):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

# secreta = "chupacabra"
# palabra = input ("ingresa palabra")
# while palabra != secreta:
#     palabra = input ("ingresa palabra")
    
    
    
# print ("Has dejado el bucle con éxito.")

secreta = "chupacabra"

while True:
    palabra = input ("ingresa palabra")
    if palabra == secreta:
        break
    print ("nee te equivocaste..")
    
    
    
print ("Has dejado el bucle con éxito.")