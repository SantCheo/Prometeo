# *	Coincide 0 o más veces con el patrón anterior.	a* → "aaa", "", "a"
# +	Coincide 1 o más veces con el patrón anterior.	a+ → "a", "aaa" (pero no "")
# ?	Coincide 0 o 1 vez con el patrón anterior (opcional).	a? → "a", ""
# {n}	Coincide exactamente n veces con el patrón anterior.	a{3} → "aaa" (pero no "aa" ni "aaaa")
# {n,}	Coincide al menos n veces con el patrón anterior.	a{2,} → "aa", "aaa", "aaaa"
# {n,m}	Coincide entre n y m veces con el patrón anterior.	a{2,4} → "aa", "aaa", "aaaa" (pero no "a" ni "aaaaa")


import re

texto = "aa abc aaaa a aaaaa"

print(re.findall(r'a*', texto))   # Coincide con "" (vacío), "a", "aa", "aaaa", etc.
print(re.findall(r'a+', texto))   # Coincide con "a", "aa", "aaaa", "aaaaa"
print(re.findall(r'a?', texto))   # Coincide con cada "a" y espacios vacíos
print(re.findall(r'a{3}', texto)) # Coincide con "aaa"
print(re.findall(r'a{2,}', texto)) # Coincide con "aa", "aaaa", "aaaaa"
print(re.findall(r'a{2,4}', texto)) # Coincide con "aa", "aaa", "aaaa"