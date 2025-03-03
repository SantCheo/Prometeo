# def hola():
#     print ("Hola mundo!")
#     print ("Bienvenido")

# hola()
# hola()

# def hola(nombre): #nombre es igual a parametro
#     print ("Hola mundo!")
#     print (f"Bienvenido {nombre}")

# hola("Alfredo") #Alfredo es igual a argumento 
# hola("Chanchito Feliz")
  

# # VARIOS PARAMETROS
# def hola(nombre, apellido):
#     print ("Hola mundo!")
#     print (f"Bienvenido {nombre}{apellido}")

# hola("Alfredo", "Rivas") 
# hola("Chanchito Feliz", "y rechoncho")

#ARGUMENTOS OPCIONALES


def hola(nombre, apellido = "y rechoncho"):
    print ("Hola mundo!")
    print (f"Bienvenido {nombre}{apellido}")

hola("Alfredo ", "Rivas") 
hola("Chanchito Feliz ", )

#ARGUMENTOS NOMBRADOS

hola(apellido= "Rivas", nombre= "cheo ")

