# Así como existe un método constructor, existe un
# método destructor cuyo cometido consiste en
# eliminar instancias de una clase. Es decir, elimina un
# objeto.

# El método destructor es el método __del__()

class Book():
#Clase para trabajar con libros
    def __init__(self, title, author = "",
        electronic = False):
        self.title = title
        self.author = author
        self.is_electronic = electronic
    def __del__(self):
        print("""Acabas de llamar al método
        destructor. El objeto acaba de ser
        eliminado""")

book1= Book("mariad")
book1.title
print (book1.title)
#Para eliminar un objeto, utilizaos la palabra reservada del
# del book1
