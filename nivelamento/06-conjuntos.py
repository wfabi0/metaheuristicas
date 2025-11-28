numeros = {6, 1, 2, 3, 4, 4, 5}

print(numeros)

numeros.add(6)

print(numeros)

numeros.remove(3)
print(numeros)

numeros.discard(3)
print(numeros)

pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}

u = pares | impares
print(u)

p2 = {4, 5, 6}
i = pares & p2
print(i)
p3 = {2, 6}
d = pares - p3
print(d)

# diferença simetrica: elementos que nao estao em ambos os conjuntos ao mesmo tempo
print(pares)
p4 = {4, 6, 10}
print(p4)
print(pares ^ p4)
