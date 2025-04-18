
# # Definición de la clase base Persona
# class Persona:
#     def __init__(self, nombre, edad, lugar):
#         # Inicialización de los atributos de la clase Persona
#         self.nombre = nombre
#         self.edad = edad
#         self.lugar = lugar

#     def descripcion(self):
#         # Método para imprimir la descripción de la persona
#         print("Nombre:", self.nombre, ", Edad:", self.edad, ", Lugar:", self.lugar)

# # Definición de la clase Empleado, que hereda de Persona
# class Empleado(Persona):
#     def __init__(self, salario, antiguedad, nombre_emp, edad_emp, lugar_epm):
#         # Llamada al constructor de la clase base (Persona) usando super()
#         super().__init__(nombre_emp, edad_emp, lugar_epm)
#         # Inicialización de los atributos específicos de Empleado
#         self.salario = salario
#         self.antiguedad = antiguedad

#     def descripcion(self):
#         # Llama al método descripcion de la clase base (Persona)
#         super().descripcion()
#         # Imprime los atributos específicos de Empleado
#         print("Salario:", self.salario, ", Antigüedad:", self.antiguedad)

# # Creación de una instancia de la clase Persona
# Angel = Persona("Angel", 43, "Malaga")
# # Llamada al método descripcion de la clase Persona
# Angel.descripcion()

# # Creación de una instancia de la clase Empleado
# Empleado1 = Empleado(2000, 2017, "Manolo", 33, "Madrid")
# # Llamada al método descripcion de la clase Empleado
# Empleado1.descripcion()



# Diferencias clave:
# Uso de Padre.__init__(self, ojos, cejas)
# En lugar de super().__init__(), llamamos directamente al constructor de Padre.
# Es una forma válida, pero menos recomendable porque si el nombre de la clase base cambia, tendríamos que modificarlo en todas las subclases.
# Mantenimiento más difícil
# Si Padre tuviera más atributos o lógica, tendríamos que asegurarnos de pasarlos manualmente en todas las subclases.

# Creamos la clase Padre
# class Padre:
#     def __init__(self, ojos, cejas):
#         # Definimos los atributos
#         self.ojos = ojos
#         self.cejas = cejas

# # Creamos la clase Hijo que hereda de Padre
# class Hijo(Padre):
#     def __init__(self, ojos, cejas, cara):
#         # Llamamos al constructor de la clase Padre sin usar super()
#         Padre.__init__(self, ojos, cejas)
#         # Agregamos el nuevo atributo para Hijo
#         self.cara = cara  

# # Instanciamos un objeto de la clase Hijo
# tomas = Hijo('Marrones', 'Negras', 'Larga')

# # Imprimimos los atributos del objeto
# print(tomas.ojos, tomas.cejas, tomas.cara)

# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, sueldo):
        # Inicialización de los atributos de la clase Empleado
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        # Método especial para representar el objeto como una cadena
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    # def mostrar_detalles(self):
    #     # Método para mostrar los detalles del empleado
    #     return self.__str__()


# Definición de la clase Gerente, que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        # Llamada al constructor de la clase base (Empleado)
        super().__init__(nombre, sueldo)
        # Inicialización del atributo específico de Gerente
        self.departamento = departamento

    def __str__(self):
        # Sobrescribe el método __str__ para incluir el departamento
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'


# Función para imprimir los detalles de un objeto
def imprimir_detalles(objeto):
    # Imprime el tipo del objeto
    print(type(objeto))
    # Llama al método mostrar_detalles del objeto
    print(objeto.mostrar_detalles())


# Creación de una instancia de Empleado
empleado = Empleado('Juan', 5000)
# Llamada a la función imprimir_detalles con el empleado
imprimir_detalles(empleado)

# Creación de una instancia de Gerente
gerente = Gerente('Karla', 6000, 'Sistemas')
# Llamada a la función imprimir_detalles con el gerente
imprimir_detalles(gerente)