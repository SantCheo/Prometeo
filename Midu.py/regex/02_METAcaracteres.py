#Cuando utilizamos el punto en una expresión regular, 
# podemos hacer coincidir cualquier carácter. Veamos esto en acción:

# import re

# texto = 'Hola mundo, Hola de nuevo. Casa, cosa, cisa, ceca, causa.'
# patron = 'H.la' # Coincide con cualquier carácter entre 'H' y 'la'
# resultados = re.findall(patron, texto)
# print(resultados)  # ['Hola']

#Supongamos que deseas buscar el punto literal en un texto. 
# Dado que el punto tiene significado especial, necesitas “escaparlo”. 
# Para ello, usamos la barra invertida (\), 
# lo que le indica a Python que el siguiente carácter es literal.

# import re

# texto = 'Mi casa es blanca. El coche es negro.'
# patron = r'\.'  # Usamos la barra invertida para buscar un punto literal
# resultados = re.findall(patron, texto)
# print(resultados)  # ['.']


# #BUSCAR DIGITOS 
# import re  # Importa el módulo de expresiones regulares

# # Texto de ejemplo con un número de teléfono
# texto = 'El número de teléfono es 68812356789'

# # Encuentra todos los dígitos individuales en el texto
# digitos = re.findall(r'\d', texto)  # Captura cada dígito por separado
# print("Dígitos individuales encontrados:", digitos)
# # Salida esperada: ['6', '8', '8', '1', '2', '3', '5', '6', '7', '8', '9']

# # Encuentra el número completo en lugar de dígitos separados
# numero_completo = re.findall(r'\d+', texto)  # Captura el número completo
# print("Número completo encontrado:", numero_completo)
# # Salida esperada: ['68812356789']

#BUSCAR CARACTERES ALFANUMERICOS 
#Si intentamos coincidir caracteres que no son alfanuméricos, 
#como símbolos especiales o espacios, no serán reconocidos por \w

# import re

# texto = 'rubius69'
# patron = r'\w+'

# resultado = re.findall(patron, texto)
# print(resultado)  # ['rubius69']

# El símbolo \s en expresiones regulares representa 
# cualquier espacio en blanco. Esto incluye:

# Espacios
# Tabulaciones
# Saltos de línea

import re
texto = 'Hola mundo!\nEste es un ejemplo.\t'
matches = re.findall(r'\s', texto)
print(matches)  # [' ', '\\n', '\\t']


#Validación de Nombres de Usuario
import re

def validar_username(username):
    patron = r'^[a-zA-Z0-9]'
    return bool(re.match(patron, username))

# Ejemplos de uso
print(validar_username('usuario1'))  # Salida: True
print(validar_username('_usuario'))   # Salida: False

# El patrón ^[a-zA-Z0-9] significa que la cadena 
# debe comenzar con un carácter alfanumérico. 
# Cualquier otro carácter, como un símbolo, hará que la validación falle.

#  Validación de Números de Teléfono

import re

def validar_telefono(telefono):
    patron = r'^\+\d{2,3}'
    return bool(re.match(patron, telefono))

# Ejemplos de uso
print(validar_telefono('+34'))        # Salida: True
print(validar_telefono('34'))         # Salida: False


#El patrón ^\+\d{2,3} permite que varias cadenas empiecen 
#con un símbolo + seguido de entre 2 a 3 dígitos.

#Validando el Final de las Cadenas

# Verificar el final de una cadena nos permite validar datos cruciales. 
# Por ejemplo, podemos asegurarnos de que una cadena 
# termine con la palabra “Mundo”. 
# Aquí hay un ejemplo:

import re

cadena_1 = 'Hola Mundo'
cadena_2 = 'Hola Mundo.'
patron = r'Mundo$'

resultado_1 = re.search(patron, cadena_1)
resultado_2 = re.search(patron, cadena_2)

print(resultado_1 is not None)  # True
print(resultado_2 is not None)  # False

# Aplicaciones Prácticas
# Este concepto es increíblemente útil en múltiples escenarios. 
# Por ejemplo, podemos validarlo después de leer registros de errores 
# o incluso al validar correos electrónicos. 
# Si queremos asegurarnos de que un correo termine con “gmail.com”, 
# podemos usar la siguiente expresión regular

import re

correo = 'usuario@gmail.com'
patron_correo = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

es_valido = re.match(patron_correo, correo)
print(es_valido is not None)  # True

# Además, podemos mejorar nuestras expresiones regulares usando cuantificadores. 
# Por ejemplo, al usar el símbolo + podemos especificar que necesitamos 
# uno o más caracteres antes de nuestro dominio.