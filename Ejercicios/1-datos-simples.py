#EJERCICIOS DATOS SIMPLES
#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

# name = input ("Indica tu nombre por favor")
# print (f"¡Hola {name}¡")

# #4
# print (((3+2)/(2*5))**2)

#5
# horas= int(input("Cuantas horas has trabahjado: "))
# coste = int (input("pago por hora: "))
# pago= horas * coste
# print (f"Tu pago total es: {pago}")


#6
# nu1 = int (input("indica un numero entero: "))

# suma = (nu1*(nu1 + 1))/2

# print (suma)

#7
# peso = float (input ( "Introdusca su peso por favor en Kg: "))
# altura = float (input ( "Introdusca su altura en metros por favor: "))

# imc= round(peso / altura**2, 2)

# print (f"Tu IMC es {imc}")

# #8
# n= int(input ("numero 1: "))
# m= int(input ("numero 2:"))

# cociente= (n//m)
# resto = (n%m)

# print (f"el {n} entre {m} da un cociente {cociente} y un resto {resto}")

#9

# c= float (input ("Qué capital va a invertir: "))
# i= float (input ("Interes anual: "))
# a= float (input ("cuantos años desea invertir el capital: "))

# cap= c * (1+i/100)**a
# # Fórmula del interés compuesto: C = P * (1 + r/100)^t

# print ("Capital obtenido en la inversión:" , round (cap, 2))

#10

# payasos = int (input ("Numero de payasos por pedido: "))

# muñecas = int (input ("Numero de muñecas por pedido: "))

# pesop= 112
# pesom= 75

# pedido = pesom * muñecas +  pesop * payasos 

# print ("peso total del pedido: ", pedido, "Kg")


#11
# ahorro = float(input("capital inicial: "))
# interes = 4

# Año1= ahorro * (1 + interes/100)**1
# Año2= ahorro * (1 + interes/100)**2
# Año3= ahorro * (1 + interes/100)**3

# print (f""" ahorros en el primer año: {round (Año1, 2)},
#        ahorros en el segundo año: {round (Año2, 2)},
#        ahorros en el tercer año: {round (Año3, 2)},""")

# #12
precio = 3.49
descuento = 0.6

barras = int (input("numero de barras de pan que no son del día: "))

coste_barra_f = precio * barras
coste_barra_no = coste_barra_f * (1- descuento)

print (f"""
       Precio de barra de pan por unidad 3.49€
       Numero de barras vendidas  {barras}
       valor                      {coste_barra_f:.2f}€
       Descuento aplicado         60%
       Precio final con descuento {coste_barra_no:.2f}
        """)



