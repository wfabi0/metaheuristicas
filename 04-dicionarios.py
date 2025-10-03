aluno = {"nome": "Ana", "idade": 20, "curso": "BSI"}

print(aluno["nome"])
print(aluno["idade"])

aluno["idade"] = 21
print(aluno)

aluno["matricula"] = "0077110"
print(aluno)

del aluno["curso"]
print(aluno)

mat = aluno.pop("matricula")
print(mat)
print(aluno)

if "idade" in aluno:
    print("Idade está presente no dicionário")
else:
    print("Idade não está presente no dicionário")

print(aluno.keys())

alunos = [{"nome": "Ana", "matricula": "0077110", "disc": ["Alg", "Mth", "BO"]}]

alunos.append({"nome": "Bruno", "matricula": "0077111", "disc": ["Alg", "Mth", "BO"]})

print(alunos)

ponto = {"x": 10, "y": 20}

print(ponto.values())

print(ponto.items())
