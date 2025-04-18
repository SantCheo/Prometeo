# class Vehiculo():
#     def __init__(self,color,ruedas):
#         self.color = color
#         self.ruedas = ruedas

#     def __str__(self):
#         return 'color: ' + self.color + ', Ruedas: ' + str(self.ruedas)
    

# class Coche (Vehiculo):
#     def __init__(self, color, ruedas, velocidad):
#         super().__init__(color, ruedas)
#         self.velocidad = velocidad

#     def __str__(self):
#         return super().__str__() + ', Velocidad (Km/hr): ' + str (self.velocidad)
    
# class Bicicleta (Vehiculo):
#         def __init__(self, color, ruedas, tipo):
#             super().__init__(color, ruedas)
#             self.tipo = tipo
        
#         def __str__(self):
#             return super().__str__() + ', Tipo: ' +self.tipo
        
# vehiculo = Vehiculo ('Rojo', 4)
# print (vehiculo)

# coche = Coche ('Azul', 4, 150)
# print (coche)

# bicicleta = Bicicleta ('Blanca', 2, 'Urbano')
# print (bicicleta)

# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, cedula, telefono):
        # Inicialización de los atributos encapsulados (usando _)
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono

    # Método para establecer el nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    # Método para obtener el nombre
    def get_nombre(self):
        return self._nombre

    # Método para establecer la cédula
    def set_cedula(self, cedula):
        self._cedula = cedula

    # Método para obtener la cédula
    def get_cedula(self):
        return self._cedula

    # Método para establecer el teléfono
    def set_telefono(self, telefono):
        self._telefono = telefono

    # Método para obtener el teléfono
    def get_telefono(self):
        return self._telefono
    

Empleado.get_telefono()