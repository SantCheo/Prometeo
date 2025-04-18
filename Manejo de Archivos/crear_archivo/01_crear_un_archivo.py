import os
os.system ("clear")

# Definimos el nombre del archivo donde se va a escribir
nombre_archivo = "ejemplo.txt"

# Abrimos el archivo en modo escritura ("w"). Si el archivo no existe, se creará.
archivo = open(nombre_archivo, "w")

# Escribimos una línea de texto en el archivo
archivo.write("hola mundo\n")

archivo.write("Estoy escribiendo en un archivo de texto \n")

# Cerramos el archivo para asegurarnos de que los cambios se guardan correctamente.
archivo.close()


print(f"El archivo {nombre_archivo} se ha creado con exito")


# Utlizando la sentencia with para manejar el archivo
# La sentencia with se encarga de cerrar el archivo automáticamente al finalizar el bloque.

with open(nombre_archivo,'w') as archivo: 
    archivo.write("hola mundo\n")
    archivo.write("Estoy escribiendo en un archivo de texto \n")

print (f"El archivo {nombre_archivo} se ha creado con exito")