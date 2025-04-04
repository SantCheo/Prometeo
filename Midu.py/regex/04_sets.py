# 🔹 Lista de sets de regex en Python
# Set de regex	Significado
# [abc]	Coincide con cualquiera de los caracteres 'a', 'b' o 'c'.
# [^abc]	Coincide con cualquier carácter excepto 'a', 'b' o 'c'. (El ^ dentro de [] significa negación).
# [0-9]	Coincide con cualquier dígito del 0 al 9 (equivalente a \d).
# [a-z]	Coincide con cualquier letra minúscula de la 'a' a la 'z'.
# [A-Z]	Coincide con cualquier letra mayúscula de la 'A' a la 'Z'.
# [a-zA-Z]	Coincide con cualquier letra mayúscula o minúscula.
# [0-9a-fA-F]	Coincide con cualquier dígito hexadecimal (0-9 y A-F).
# [aeiouAEIOU]	Coincide con cualquier vocal, mayúscula o minúscula.
# [\w]	Coincide con cualquier carácter alfanumérico (a-z, A-Z, 0-9, _).
# [\W]	Coincide con cualquier carácter NO alfanumérico.
# [\d]	Coincide con cualquier dígito (0-9).
# [\D]	Coincide con cualquier carácter que NO sea un dígito.
# [\s]	Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea).
# [\S]	Coincide con cualquier carácter que NO sea espacio en blanco.



import re

# Coincide con cualquier vocal
patron = r"[aeiou]"
print(re.findall(patron, "Python es increíble"))  
# ➝ ['o', 'e', 'i', 'i', 'e', 'i', 'e']

# Coincide con cualquier dígito
patron = r"[0-9]"
print(re.findall(patron, "Mi número es 12345"))  
# ➝ ['1', '2', '3', '4', '5']

# Coincide con caracteres que NO sean vocales
patron = r"[^aeiou]"
print(re.findall(patron, "Python es increíble"))  
# ➝ ['P', 'y', 't', 'h', 'n', ' ', 's', ' ', 'n', 'c', 'r', 'b', 'l']

# Coincide con letras mayúsculas
patron = r"[A-Z]"
print(re.findall(patron, "Hola Mundo PYTHON"))  
# ➝ ['H', 'M', 'P', 'Y', 'T', 'H', 'O', 'N']
