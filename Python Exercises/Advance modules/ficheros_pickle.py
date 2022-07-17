import pickle

lista = [1,2,3,4,5]

fichero = open('lista.pckl', 'wb')

pickle.dump(lista, fichero)

fichero.close()

del(fichero)

fichero = open('lista.pckl', 'rb')

lista = pickle.load(fichero)

print(lista)

fichero.close()

del(fichero)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self) -> str:
        return self.nombre

nombres = [ 'Sergio', 'Mario', 'Marta' ]

personas = []

for n in personas:
    p = Persona(n)
    personas.append(p)

fichero = open('personas.pckl', 'wb')

pickle.dump(personas, fichero)

fichero.close
del(fichero)

fichero = open('personas.pckl', 'rb')

personas = pickle.load(fichero)

fichero.close

for persona in personas:
    print(p)