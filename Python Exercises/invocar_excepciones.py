def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error!")
    except ValueError:
        print("Error! desde la excepción")
mi_funcion()