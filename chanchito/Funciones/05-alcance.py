saludo = "Hola global"
# def saludar():
#     saludo= "Hola mundo"
#     print ( saludo )

# def saluda ():
#     saludo = "hola chanchito"
#     print (saludo)

# saludar()
# saluda () 
# print (saludo)

#No usar variables globales en un alcance local 

def saluda ():
    global saludo
    print (saludo)

saludo()
print (saludo)