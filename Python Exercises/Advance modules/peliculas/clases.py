# The class Pelicula has a constructor that takes three arguments, and a method that returns a string.
# 
# 
# The class Catalogo has a constructor that loads a list of Pelicula objects from a file, a method
# that adds a Pelicula object to the list, a method that displays the list of Pelicula objects, a
# method that saves the list of Pelicula objects to a file, and a destructor that saves the list of
# Pelicula objects to a file
from io import open
import pickle

class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} películas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()
    
    def __del__(self):
        self.guardar()