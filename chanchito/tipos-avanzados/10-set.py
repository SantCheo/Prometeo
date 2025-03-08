# SET significa grupo o conjunto
primer = {1,1,2,2,3,3,4,4} # los elementos no se repiten, solo guarda uno #{1, 2, 3, 4}
primer.add (5)# agregar un nuevo elemnto #{1, 2, 3, 4, 5}
primer.remove (1) #borrar elemento #{2, 3, 4, 5}
print (primer)


#Convertir lista en Set
segundo= [3,4,5,6]
segundo = set(segundo)

print (segundo)

# Unir set | 
#tercer = primer | segundo
#print (tercer) #{2, 3, 4, 5, 6}

#Intercepcion &
print (primer & segundo) #Devuelve los elementos en común {3, 4, 5}

# Diferencia - : Elimina los elemendos del set (segundo) que se encuentren en el set (primer)
print (primer - segundo) 

#Diferencia simetrica ^ : Elimina los elementos en común en ambos set, dejando los elementos no compartidos
print (primer ^segundo)

 