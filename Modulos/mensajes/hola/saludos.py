def saludar():
    print("Hola, te saludo desde saludos.saludar()")
    
class Saludo:
    def __init__(self):
        print("Te saludo desde def init")  
        
print(__name__)
if __name__ == '__main__':
    saludar()