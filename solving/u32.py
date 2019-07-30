a = [1, 2, 3]
b = a
c = a[:]
d = (1, 2, 3)
e = d
f = d[:]
g = {1, 2, 3}
h = g
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
print(id(g))
print(id(h))