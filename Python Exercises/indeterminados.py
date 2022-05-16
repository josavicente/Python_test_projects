def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

print(indeterminados_posicion(5, "hola", [1,2,3,4,5]))

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

print(indeterminados_nombre(n=5, c="hola", l=[1,2,3,4,5]))