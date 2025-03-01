# n1 = int(input("ingresa el primer numero"))
# n2 = int(input("ingresa el segundo numero"))

# suma= n1 + n2
# resta = n1 - n2
# multi= n1 * n2
# divi= n1 / n2

# mensaje = f"""
# Para los numeros ¨{n1} y {n2}, 
# el resultado de la suma es {suma},
# el resultado de la resta es {resta},
# el resultado de la muntiplicación es {multi},
# el resultado de la  es divisió es {divi}
# """
# print (mensaje)


print ("""
Bienvenido a la calculadora, 
Para salir escribe salir
Las opreciones son: Suma, Resta, División y Multiplicación
       
""")

resultado = ""
while True:
    if not resultado:
        resultado = input ("ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int ( resultado)
    op = input ("ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input ("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int ( n2)

    if op.lower()== "+":
        resultado += n2
    elif op.lower()== "-":
        resultado -= n2
    elif op.lower()== "*":
        resultado *= n2
    elif op.lower()== "/":
        resultado /= n2
    else:
        print ("Operación no valida")
        break
print (f"""El resultado es: {resultado}""")
    
