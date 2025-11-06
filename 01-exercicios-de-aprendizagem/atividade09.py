matriz = [[], [], [], [], [], []]

for i in range(5):
    for j in range(5):
        numero = int(input(f"Digite o número para a posição [{i}][{j}]: "))
        matriz[i].append(numero)

print("\nResultado da Matriz: ")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()
