#Las regex te permiten realizar búsquedas avanzadas en grandes volúmenes de texto. 
# No importa si estás buscando emails, números de teléfono, o patrones complejos, 
# la síntesis y flexibilidad de las regex te harán la vida más fácil.


#Encontrando emails en un texto
import re

# Definir patrón de regex para el email
patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Ejemplo de texto
texto = 'Puedes contactarnos en info@ejemplo.com o soporte@ejemplo.org'

# Buscar emails
emails_encontrados = re.findall(patron_email, texto)
print(emails_encontrados)  # Muestra: ['info@ejemplo.com', 'soporte@ejemplo.org']

# Validación de datos
# Las expresiones regulares también son excelentes para validar datos. 
# Por ejemplo, puedes asegurarte de que un número telefónico sigue el 
# formato correcto o que un email es válido.

# Validando un número telefónico

import re

# Definir patrón para un número telefónico
patron_telefono = r'^\+?\d{1,3}?[-. ]?\(?\d{1,4}?\)?[-. ]?\d{1,4}[-. ]?\d{1,9}$'

# Ejemplo de número
numero = '+34 912 345 678'

# Validar número
valido = re.match(patron_telefono, numero)
print(valido is not None)  # Muestra: True

# Manipulación del texto
# Además de buscar y validar, las regex te permiten modificar 
# y reemplazar partes de un texto fácilmente. 
# Esta capacidad es especialmente útil en tareas de limpieza de datos.


# Reemplazando números de teléfono

import re

# Ejemplo de texto
texto = 'Hola, mi número es 555-1234 y mi email es ejemplo@dominio.com'

# Reemplazar número de teléfono
nuevo_texto = re.sub(r'\d{3}-\d{4}', 'XXX-XXXX', texto)
print(nuevo_texto)  # Muestra: 'Hola, mi número es XXX-XXXX y mi email es ejemplo@dominio.com'

import re

texto = 'Este es un texto de evaluación sobre IA y su impacto.'
patron = 'IA'


# Ejemplo de búsqueda de coincidencia
coincidencias = re.search(patron, texto)
if coincidencias:
        print(f'Patrón encontrado en la posición {coincidencias.start()}-{coincidencias.end()}')
else:
        print('Patrón no encontrado.')

#Encontrando Múltiples Coincidencias

texto = 'Me gusta Python. Python es increíble. Aprender Python es divertido.'
#Para encontrar todas las coincidencias del patrón “Python”, usaremos el método findall():
resultados = re.findall('Python', texto)
print(f'Número de coincidencias: {len(resultados)}')
print('Coincidencias encontradas:', resultados)


#MODIFICADORES USO DE IGNORATECASE
import re

text = 'La IA está cambiando el mundo. La ia es una herramienta poderosa.'
pattern = r'ia'

# Búsqueda sensible a mayúsculas
found_case_sensitive = re.findall(pattern, text)
print('Encontrado (sensible a mayúsculas):', found_case_sensitive)

# Búsqueda ignorando mayúsculas y minúsculas
found_ignore_case = re.findall(pattern, text, re.IGNORECASE)
print('Encontrado (ignora mayúsculas/minúsculas):', found_ignore_case)

#REPLAZAR TEXTO, METODO SUB
# El método sub() se utiliza para reemplazar partes de un texto que coinciden con un patrón regex.
import re

texto = 'Hola mundo, hola de nuevo'
nuevo_texto = re.sub(r'hola', 'adiós', texto, flags=re.IGNORECASE)

print(nuevo_texto)  # Salida: 'adiós mundo, adiós de nuevo'

# COUNT PARA LIMITAR EL NÚMERO DE REEMPLAZOS
#Por defecto, sub sustituye todas las coincidencias, 
# pero puedes limitarlo usando el argumento count.
import re

texto = 'Hola mundo, hola de nuevo'
nuevo_texto = re.sub(r'hola', 'adiós', texto, count=1, flags=re.IGNORECASE)

print(nuevo_texto)  # Salida: 'adiós mundo, hola de nuevo'