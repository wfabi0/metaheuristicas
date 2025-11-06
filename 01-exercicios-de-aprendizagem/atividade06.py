pessoas = []

count = 1
for i in range(5):
    nome = input(f"Digite o {count} nome da pessoa: ")
    idade = int(input(f"Digite a {count} idade da pessoa: "))
    pessoas.append((nome, idade))
    count += 1

maiores_de_idade = []
print("\nPessoas Cadastradas: ")
for pessoa in pessoas:
    nome, idade = pessoa
    if idade >= 18:
        maiores_de_idade.append(pessoa)
    print("Nome: ", nome)
    print("Idade: ", idade)
    print()

print("----------------------------")
print("Pessoas maiores de idade: ")
print()

for pessoa in maiores_de_idade:
    nome, idade = pessoa
    print("Nome: ", nome)
    print("Idade: ", idade)
    print()
