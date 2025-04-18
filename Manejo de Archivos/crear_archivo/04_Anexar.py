print ("*** ANEXAR ARCHIVO ***")

# 'a': Append (solo escritura al final)

# 'a+': Append y lectura (permite leer y escribir)

# 'w': Write (sobrescribe el archivo completo)

# 'r+': Lectura y escritura (sin truncar el archivo)

nombre_archivo= "ejemplo.txt"

with open (nombre_archivo, "a") as archivo:
     archivo.write("\n Estoy añadiendo nueva información al archivo, sin modificar la anterior\n")
     archivo.write("Eso es todo amigos, Adios\n")

print (f"El archivo {nombre_archivo} dispone información nueva")