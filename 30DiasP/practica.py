#Sistema de Gestión de Biblioteca

#Clase libro con los atributos a manejar 
class Libro():
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def mostrar(self):
            estado = "si" if self.disponible else "no"
            return (f"-Titulo: {self.titulo} -Autor: {self.autor}  \n ISBN: {self.isbn}  (Disponible: {estado})")
    
    def prestar(self):
        if self.disponible:
            self. disponible = False
            print (f"El libro {self.titulo} prestado con éxito.")
        else:
            print(f"El Libro {self.titulo} no está disponible")

    def devolver (self):
        if not self.disponible:
            self.disponible = True
            print (f"Libro {self.titulo} devuelto con exito")
        else:
            print (f"Libro {self.titulo} ya se encontraba disponible")



class Biblioteca():
    def __init__(self):
        self.inventario = [] 
# Metodo para agragar nuevos libros a la Biblioteca     
    def agregar (self, titulo, autor,isbn):
        nuevo_libro = Libro (titulo, autor, isbn)
        self.inventario.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado con éxito.")
# Metodo para mostrar el inventario de la Biblioteca 
    def mostrar(self):
        if not self.inventario:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.inventario:
                print (libro.mostrar())
# Metodo para buscar libro por ISBN, utlizamos el parametro mostrar= True para imprimir 
    def buscar(self, isbn, mostrar=True):
        for libro in self.inventario:
            if libro.isbn == isbn:
                if mostrar:
                    print(libro.mostrar())
                return libro
        print("Error: ISBN no encontrado.") if mostrar else None
        return None
#Metodo para prestar un libro usando el ISBN, llama al metodo buscar usando el parametro mostrar = false
    def prestar (self, isbn):
        libro = self.buscar(isbn, mostrar=False)
        if libro:
            libro.prestar()
        else:
            print("Error: ISBN no encontrado.")
# Metodo para devolver el libro, llama al metodo buscar usando el parametro mostrar = false
    def devolver (self, isbn):
        libro = self.buscar (isbn, mostrar = False)
        if libro:
            libro.devolver()
        else:
            print ("Error, libro no encontrado")
            
                                                                                                                    
    

biblioteca = Biblioteca ()                                                                                                                                                                                                                                                                                                         

def menu ():
    while True:
        print ("Bienvenido al Sistema de Gestión de Biblioteca")
        print ("1. Agregar libro")
        print ("2. Prestar libro")
        print ("3. Devolver libro")
        print ("4. Mostrar libros")
        print ("5. Buscar")
        print ("6. Salir")
        opcion = ( input ("Elige una opción: "))

        if opcion == "1":
            titulo = input("Titulo: ")
            autor = input ("Autor: ")
            isbn = input ("ISBN: ")
            biblioteca.agregar(titulo,autor,isbn)
        
        elif opcion == "2":
            isbn = input ("Ingresa el ISBN: ")
            biblioteca.prestar(isbn)

        elif opcion == "3":
            isbn = input ("Ingresa el ISBN: ")
            biblioteca.devolver(isbn)

        elif opcion == "4":
            biblioteca.mostrar()

        elif opcion == "5":
            isbn = input ("Ingresa el ISBN: ")
            biblioteca.buscar(isbn)

        elif opcion == "6":
            print ("Saliendo de la Biblioteca \nGracias por visitarnos")
            break
        else:
            print ("\nOpción no válida, vuelve a intentar\n")

if __name__ == "__main__":
    menu()

        











