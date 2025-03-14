class Micoche():
    def __init__(self):
        self.largo = 25 
        self.ancho = 200
        self.ruedas = 4
        self.peso  = 120
        self.is_enMarcha = False
        self.color = "Verde"
    def arrancar(self):             
            self.is_enMarcha = True 
            return ""   
    def estado(self): 
            if (self.is_enMarcha == True): 
                return "El coche está arrancado" 
            else: 
                return "El coche está parado"     
            
coche = Micoche()
print (coche.arrancar(), coche.estado())

print (coche.ruedas, coche.ancho)
print (coche.estado())

# class Usuario():
#     nombre = "Angel"
#     edad = 46
#     login = "admin"
#     password = "1234"
#     email = "angel@loquesea.com"
#     telefono = 666666

#     def resumen (self):
#         print (f"""Los datos del usuario son: 
#                nombre: {self.nombre}
#                edad: {self.edad}
#                login: {self.login}
#                password: {self.password}
#                email: {self.email}
#                telefono: {self.telefono}""")
    
#     def cambiaEdad (self):
#         edadIntroducida = int (input("Introduce edad entre 18 - 100: "))

#         if 18< edadIntroducida < 100: 
#                 self.edad = edadIntroducida
#                 print ("Edad introducida correcta")
#                 return ""
#         else: 
#              print ("La edad introducida no es correcta.")
#              self.cambiaEdad()
#              return 
        
#     def muestraEdad (self):
#          print ("La Edad del usuario es: ", self.edad, "años.")
    
# Administrador = Usuario()

# print (Administrador.resumen())
# print (Administrador.cambiaEdad())
# print (Administrador.muestraEdad())


    