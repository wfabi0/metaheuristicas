nome = "Fábio"  # string
sala = 3  # inteiro
altura = 1.78  # float
is_student = False  # booleano
notas = [8.5, 9.0, 7.5]  # lista
numeros = (1, 2, 3)  # tupla
pessoa = {"nome": "Fábio", "disciplina": "Metaheurísticas"}  # dicionário
cores = {"vermelho", "verde", "azul"}  # conjunto

print(
    "Nome "
    + nome
    + " sala: "
    + str(sala)
    + " altura: "
    + str(altura)
    + ", é estudante: "
    + str(is_student)
)

print(f"Notas: {notas}")
print(f"Números: {numeros}")
print(f"Pessoa: {pessoa}")
print(f"Cores: {cores}")
