def saludar():
    print("Hola, te saludo desde saludos.saludar()")


def prueba():
    print("esto es una prueba de la nueva versión")
class Saludo:
    def __init__(self):
        print("Te saludo desde def init")  
        
print(__name__)
if __name__ == '__main__':
    saludar()