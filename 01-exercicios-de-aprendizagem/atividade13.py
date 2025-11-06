def apenas_pares(lista):
    return [x for x in lista if x % 2 == 0]


lista = []
for i in range(5):
    n = int(input(f"Digite o {i + 1}º número: "))
    lista.append(n)

print(f"O números pares são: {apenas_pares(lista)}")
