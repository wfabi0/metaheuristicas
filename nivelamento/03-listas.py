frutas = ["maçã", "banana", "uva"]

print(frutas)

f1 = frutas[0]
f2 = frutas[2]

print(f1)
print(f2)

frutas.append("melancia")

print(frutas)

frutas.insert(1, "pera")

print(frutas)

frutas.remove("uva")

print(frutas)

del frutas[0]

print(frutas)

numeros = [10, 20, 30, 40, 50]
numeros = numeros[1:4]

print(12)

print(numeros[:3])
print(numeros[-2:])

listas1 = [1, 2, 3]
listas2 = [4, 5]

listas_total = listas1 + listas2

print(listas_total)

idades = [15, 22, 30, 18]

print(len(idades))
print(max(idades))
print(min(idades))
print(sum(idades))

t = 3 * idades
print(t)

if 20 in idades:
    print("Tem")
else:
    print("Não tem")

