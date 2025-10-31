pessoas = []

for i in range(2):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    pessoas.append((nome, idade))

maiores_de_idade = []
print("Pessoas Cadastradas: ")
for pessoa in pessoas:
    nome, idade = pessoa
    if idade >= 18:
        maiores_de_idade.append(pessoa)
    print("Nome: ", nome)
    print("Idade: ", idade)
    print()

print()
print("Pessoas maiores de idade: ")
print()
print()

for pessoa in maiores_de_idade:
    nome, idade = pessoa
    print("Nome: ", nome)
    print("Idade: ", idade)
    print()
