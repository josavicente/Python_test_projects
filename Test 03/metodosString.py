texto = "Este es el texto de Federico"

resultado = texto.upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("t")
print(resultado)


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])

print(e)


resultado = texto.find("s")
print(resultado)

resultado = texto.find("g")
print(resultado)

resultado = texto.replace("Federico", "Josa")
print(resultado)

resultado = texto.replace("e", "x")
print(resultado)