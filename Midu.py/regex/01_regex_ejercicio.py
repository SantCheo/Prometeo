
# # Encuentra todas las ocurrencias de la palabra “midu” en un texto
# # y muestra en qué posiciones se encuentran. ¡Manos a la obra!

# import re

# valor = "midu"
# texto = "midu es un gran profesor de Python. midu es genial. midu es el mejor."

# coincidencias = re.finditer(valor, texto)
# for coincidencia in coincidencias:
#     print (f"Patrón  '{coincidencia.group()}'  encontrado en la posición {coincidencia.start()}-{coincidencia.end()}")

# Finalmente, para practicar, intenta crear una expresión regular 
# que verifique nombres de archivos con la extensión .txt 
# en una lista de archivos. Esto te ayudará a reafirmar lo que aprendiste.




# files = 'file1.txt, file2.pdf, mudu-of.webp, secret.txt'

# def encontrar_txt(files):
#     import re 
#     patron = r'\w+\.txt' # coincide con cualquier palabra seguida de .txt
#     resultados = re.finditer(patron, files)
#     for resultado in resultados:
#         if resultado:
#             print (f"El archivo {resultado.group()} es una archivo de texto")
#         else:
#             None


# print (encontrar_txt(files) )


import re 
files = 'file1.txt, file2.pdf, mudu-of.webp, secret.txt'
patron = r'\w+\.txt' # coincide con cualquier palabra seguida de .txt
resultados = re.findall(patron, files)

print(resultados if resultados else None)

