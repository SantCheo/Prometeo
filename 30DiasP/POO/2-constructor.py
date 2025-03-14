class Micoche():
    # # Declaración del constructor con parámetros
    def __init__(self, largo, ancho,ruedas, peso, color, is_enMarcha):
        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso  = peso
        self.is_enMarcha = is_enMarcha
        self.color = color 
            
# Declaración de dos instancias de clase pasándoles
#los parámetros requeridos en el constructor.          
# 
coche1= Micoche (400, 160, 4, 1200, True, "Amarillo")

coche2 = Micoche (420, 150, 5, 1500, False, "Rojo")