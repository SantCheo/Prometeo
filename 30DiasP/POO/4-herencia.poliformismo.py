class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True

    def arrancar(self):
        self.arrancado = True
        self.parado = False

    def parar(self):
        self.parado = True
        self.arrancado = False

    def resumen(self):
        print(f"""Marca: {self.marca},
                Modelo: {self.modelo},
                Color: {self.color},
                Está arrancado:{self.arrancado},
                Está parado: {self.parado}""")
              

miCoche = Vehiculo("Renault", "Megane")
miCoche.arrancar()
miCoche.color= "Amarillo"
miCoche.resumen()

class Moto (Vehiculo):
    is_carenado = False
    #Método propio de la clase Moto, no heredado del padre.
    def poner_carenado(self):
        self.is_carenado = True
        
    def resumen(self):
        print(f"""El modelo es una moto
                Marca: {self.marca}
                Modelo: {self.modelo}
                Color: {self.color}
                Está arrancado: {self.arrancado}
                Está parado: {self.parado}
                Tiene carenado: {self.is_carenado}""")

miMoto = Moto("Kawasaki", "Ninja")

miMoto.resumen()
class kwad(Moto):
    pass
miKwad = kwad("Linhai", "LH 500")
miKwad.resumen()
miKwad.estado()