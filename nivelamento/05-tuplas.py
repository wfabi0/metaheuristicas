coordenada = (10, 20)

print(coordenada)

print(coordenada[0])
print(coordenada[1])

cores = ("vermelho", "vermelho", "verde", "azul")

print(len(cores))

print(cores.count("vermelho"))

i = cores.index("verde")

print(i)

print(cores[1:3])
print(cores[:2])
print(cores[-2:])

ponto = (99, 200)

# desempacotamento
x, y = ponto
print(x, y)

t = (10, 20, (30, 40))
print(t)

print(t[2][1])

t1 = (1, 2, 3)
t2 = (4, 5)
r = t1 + t2
print(r)

t3 = t1 * 3
print(t3)

if "verde" in cores:
    print("tem verde")
else:
    print("nao")
