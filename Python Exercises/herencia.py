import py_compile


class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    def __str__(self) -> str:
        return """
        REFENCIA \t{}
        NOMBRE \t\t{}
        PVP \t\t{}
        DESCRIPCION \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __str__(self) -> str:
        return """
        REFENCIA \t{}
        NOMBRE \t\t{}
        PVP \t\t{}
        DESCRIPCION \t{}
        PRODUCTOR \t{}
        DISTRIBUIDOR \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)
    
class Libro(Producto):
    autor = ""
    isbn = ""
    
    def __str__(self) -> str:
        return """
        REFENCIA \t{}
        NOMBRE \t\t{}
        PVP \t\t{}
        DESCRIPCION \t{}
        AUTOR \t\t{}
        ISBN \t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.autor, self.isbn)
    
a = Adorno(2034,"Vaso adornado", 15, "Vaso adornado")
print(a)

al = Alimento(2035,"Botella", 10, "Botella")
al.productor = "Productor"
al.distribuidor = "Distribuidor"
print(al)

li = Libro(2036,"Libro", 10, "Libro")
li.autor = "Autor"
li.isbn = 2141234512342

print(li)

productos = [a, al]
productos.append(li)

for p in productos:
    print(p)
    
    
def rebajar_producto(p, rebaja):
    """Devuelve un producto con una rebaja"""
    p.pvp = p.pvp - (p.pvp/100)* rebaja
    return p

al_rebajado = rebajar_producto(al, 10)
print(al_rebajado)

copia_al = al
copia_al.referencia = 2038

print(copia_al)
print(al)