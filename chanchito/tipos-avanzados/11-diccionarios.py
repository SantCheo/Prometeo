punto= {"x":25, 
        "y":50}
print (punto)
print (punto ["x"])
print (punto ["y"])

#agregar un nuevo elemento
punto ["z"] = 45
print (punto)

if "lala" in punto:
    print ("encontre lala", punto ["lala"])


#Metodo .get  : llamar un elento del diccionario
print (punto.get("x"))
print (punto.get("lala"))
print (punto.get("lala", 97)) # Si no existe el elemento se puede indicar que imprima uno por defecto (97)

# del : Eliminar elemento
del punto ["x"]
del (punto ["y"])


