import random


def gera_solucao(n):
    s = []
    for i in range(n):
        s.append(random.randint(0, 1))
    return s


def avalia_solucao(s):
    return sum(s)


def heuristica_aleatoria(n, iteracoes):
    melhor = None
    avaliacao = -1
    for _ in range(iteracoes):
        nova_solucao = gera_solucao(n)
        avaliacao_nova_solucao = avalia_solucao(nova_solucao)
        if avaliacao_nova_solucao > avaliacao:
            melhor = nova_solucao
            avaliacao = avaliacao_nova_solucao

    return melhor, avaliacao, iteracoes


print(heuristica_aleatoria(50, 1000000))
