def maior_valor(lista):
    return max(lista)


lista = []
for i in range(5):
    n = int(input(f"Digite o {i + 1}º número: "))
    lista.append(n)

print(f"O maior valor é {maior_valor(lista)}")
