conjunto = set()
conjunto = {1,2,3,4,5,6,7,8,9}

conjunto.add(0)

print(conjunto)

grupo = { 'josa', 'joao', 'Nico'}

print ('josa' in grupo)

pila = [3,4,5]
pila.append(6)
pila.append(7)

print(pila)

print(pila.pop())
print(pila)

from collections import deque
cola = deque()
print(cola)

cola = deque ([2,3,4,5,6,7,8])
print(cola)
cola.append(10)
print(cola)
cola.append(25)
print(cola)

print(cola.popleft())
print(cola)