print ("*** Leer Archivo ***")

# 'r': Lectura (default)

# 'rb': Lectura en modo binario

# 'r+': Lectura y escritura


nombre_archivo = "ejemplo.txt" 

#Leer archivo utlizando el metodo readlines()
# Abrimos el archivo en modo lectura ('r') con el nombre que esté guardado en la variable 'nombre_archivo'
# La instrucción 'with' asegura que el archivo se cierre automáticamente después de que se termine de usar
with open(nombre_archivo, 'r') as archivo: 
    
    # Leemos todas las líneas del archivo y las guardamos en una lista llamada 'lineas'
    lineas = archivo.readlines()
    
    # Recorremos cada línea en la lista 'lineas'
    for linea in lineas:
        # Imprimimos la línea eliminando los espacios en blanco al inicio y al final (incluye saltos de línea \n)
        print(linea.strip())
     

#Leer archivo utlizando el metodo read()
print ("***Leeyendo archivo con read()***")

with open(nombre_archivo, 'r') as archivo: 
    
    # Leemos todas las líneas del archivo y las guardamos en una lista llamada 'lineas'
    print (archivo.read().strip())
