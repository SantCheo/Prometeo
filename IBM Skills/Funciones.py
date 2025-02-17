#La sintaxis necesaria para declarar una función es la 
#siguiente
# def nombre_de_la_funcion(arg1,arg2,arg...n):

G = 'Esta variable es de ámbito Global' 
def f1(): 
E='Esta variable es local a f1. 
Enclosing a f2' 
def f2(): 
L = 'Esta variable es local a f2' 
print(L, E, G, sep = '\n') 
f2() 
f1() 

