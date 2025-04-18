print ("ABRIR ARCHIVO EXCLUSIVO")
# Definimos el nombre del archivo que queremos crear
nombre_archivo = "Exclusivo.txt"

# Intentamos crear el archivo usando un bloque try-except para manejar errores
try:
    # Abrimos el archivo en modo exclusivo ('x'), que falla si el archivo ya existe
    with open(nombre_archivo, 'x') as archivo: 
        
        archivo.write("hola mundo\n")
        archivo.write("Este es un archivo exclusivo \n")
        # Mostramos mensaje si el archivo se ha creado correctamente
        print(f"El archivo {nombre_archivo} se ha creado con exito")

# Si el archivo ya existe, se lanza una excepción FileExistsError
except FileExistsError as e:
    # Se informa al usuario que no se pudo crear el archivo porque ya existe
    print(f"El archivo {nombre_archivo} ya existe, no se puede crear un archivo exclusivo")
    # Se muestra el detalle técnico del error
    print(f"Detalle del error: {e}")