
from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]

Counter(l)

# print(Counter(l))


p = "palabra"

# print(Counter(p))


animales = "gato perro canario perro canario perro"

# print(Counter(animales.split()))

c = Counter(animales.split())

# print(c.most_common())


l = [10,20,30,40,10,20,30,10,20,10]

c = Counter(l)

c.items()

print (c.keys())
print (c.values())
print(sum(c.values()))
print(list(c))
print(dict(c))
print(set(c))

from collections import defaultdict
# Creating a dictionary with a default value of float.
d = defaultdict(float)


from collections import OrderedDict

n = OrderedDict()

n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

t = (20,40,60)

from collections import namedtuple

Persona = namedtuple('Persona', 'nombre apelido edad')

p = Persona(nombre='Josa', apelido='Vicente', edad=42)
