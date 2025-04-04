# Lista de Metacaracteres en Expresiones Regulares (Regex)

# .	Coincide con cualquier carácter, excepto salto de línea (\n).	a.b → "acb", "a9b", "a_b" (pero no "ab")
# ^	Coincide con el inicio de una línea o cadena.	^Hola → "Hola mundo" (pero no "Mundo Hola")
# $	Coincide con el final de una línea o cadena.	mundo$ → "Hola mundo" (pero no "mundo Hola")
# *	Coincide 0 o más veces con el patrón anterior.	ab*c → "ac", "abc", "abbc", "abbbc"
# +	Coincide 1 o más veces con el patrón anterior.	ab+c → "abc", "abbc", "abbbc" (pero no "ac")
# ?	Coincide 0 o 1 vez con el patrón anterior.	ab?c → "ac", "abc" (pero no "abbc")
# {n}	Coincide exactamente n veces.	a{3} → "aaa" (pero no "aa" ni "aaaa")
# {n,}	Coincide al menos n veces.	a{2,} → "aa", "aaa", "aaaa"
# {n,m}	Coincide entre n y m veces.	a{2,4} → "aa", "aaa", "aaaa"
# []	Coincide con cualquier carácter dentro de los corchetes.	[aeiou] → "a", "e", "i", "o", "u"
# `	`	Alternativa (equivalente a "o").
# ()	Agrupa patrones y extrae coincidencias.	(ab)+ → "ab", "abab", "ababab"
# \d	Coincide con dígitos (0-9).	\d+ → "123", "456" en "abc 123 def 456"
# \D	Coincide con cualquier carácter que no sea un dígito.	\D+ → "abc", "def" en "abc 123 def"
# \s	Coincide con espacios en blanco (\t, \n, \r, ).	\s+ → " " en "Hola Mundo"
# \S	Coincide con cualquier carácter que no sea un espacio.	\S+ → "Hola", "Mundo"
# \w	Coincide con cualquier carácter alfanumérico (a-z, A-Z, 0-9, _).	\w+ → "Hola123" en "Hola123!"
# \W	Coincide con cualquier carácter que no sea alfanumérico.	\W+ → "!" en "Hola123!"
# \b	Coincide con un límite de palabra (inicio o fin de palabra).	\bHola\b → "Hola" (pero no "Hola123")
# \B	Coincide dentro de una palabra (no en los bordes).	\Bola → "Hola" (pero no "ola" por sí sola)


import re  

texto = "Hola, mi número es 123 y vivo en la calle 45B."

# Buscar palabras
print(re.findall(r'\b\w+\b', texto))  # ['Hola', 'mi', 'número', 'es', '123', 'y', 'vivo', 'en', 'la', 'calle', '45B']

# Buscar solo los números
print(re.findall(r'\d+', texto))  # ['123', '45']

# Buscar palabras que empiezan con "H" o "c"
print(re.findall(r'\b[Hc]\w+\b', texto))  # ['Hola', 'calle']

# Reemplazar dígitos con "X"
print(re.sub(r'\d', 'X', texto))  # "Hola, mi número es XXX y vivo en la calle XXB."
