alunos = []

while True:
    nome = input("Digite o nome do aluno: ")
    if nome.lower() == "sair":
        print("Cadastro finalizado.")
        break
    try:
        nota = float(input("Digite a nota do aluno: "))
    except ValueError:
        print("Nota inválida. Tente novamente.")
        continue

    aluno = {"nome": nome, "nota": nota}
    alunos.append(aluno)
    print(f"Aluno {aluno['nome']} cadastrado com nota {aluno['nota']}.")

if alunos:
    media = sum(aluno["nota"] for aluno in alunos) / len(alunos)
    print("Média da turma:", media)

    print("Alunos acima da média:")
    for aluno in alunos:
        if aluno["nota"] > media:
            print(f"{aluno['nome']} - Nota: {aluno['nota']}")
else:
    print("Nenhum aluno cadastrado.")
