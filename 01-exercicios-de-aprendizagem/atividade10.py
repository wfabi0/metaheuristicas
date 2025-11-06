matriz = [[], [], [], [], [], []]

for i in range(5):
    for j in range(5):
        numero = int(input(f"Digite o número para a posição [{i}][{j}]: "))
        matriz[i].append(numero)

identidade = True
for i in range(5):
    for j in range(5):
        if i == j:
            if matriz[i][j] == 0:
                identidade = False
                break

        if i != j:
            if matriz[i][j] == 1:
                identidade = False
                break

print("\nResultado da Matriz: ")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()

print(f"Sua matriz {('é' if identidade else 'não é')} identidade")
