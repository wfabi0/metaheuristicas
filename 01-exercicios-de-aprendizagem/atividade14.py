def inicia_com_a(lista):
    return [item for item in lista if item.lower().startswith("a")]


lista = []
for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    lista.append(nome)

print(f"O nomes que começam com 'A' são: {inicia_com_a(lista)}")
