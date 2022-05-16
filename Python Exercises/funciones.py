def saludar():
    print("Hola!")

saludar()

def dibujar_tabla_del_5():
    for i in range(10):
        print("5 *", i, "=", 5*i)

dibujar_tabla_del_5()


def test():
    return "Una cadena", 20, [1,2,3,4,5,6]

c,n,l = test()
print(test())


def suma(a,b):
    return a + b

s = suma(2,4)

print(s)