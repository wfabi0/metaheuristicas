alunos = []

for i in range(10):
    nome = input(f"Digite o nome do {i + 1} aluno: ")
    nota = float(input("Digite a nota do aluno (0-10): "))
    if nota < 0 or nota > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10.")
    else:
        alunos.append({"nome": nome, "nota": nota})

for aluno in alunos:
    if aluno["nota"] >= 6:
        print("Nome do aluno:", aluno["nome"])
        print("Nota do aluno:", aluno["nota"])
        print()
