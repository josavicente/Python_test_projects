# método tradicional

from csv import list_dialects


lista = []

for letra in 'casa':
    lista.append(letra)

print(lista)

#método con comprensión de listas

lista = [letra for letra in 'casa']

print(lista)

#método tradicional

lista = []

for numero in range(0,11):
    lista.append(numero **2)

print(lista)


# Método con comprehensión
list = [numero**2 for numero in range(0,11)]
print(lista)
#método tradicional
lista=[]

for numero in range(0,10):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

# Método comprehensión

lista = [ numero for numero in range(0,10) if numero % 2 == 0 ]
print(lista)