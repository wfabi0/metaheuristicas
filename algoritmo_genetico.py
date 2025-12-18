import math
import random


def bin_float(bits, a, b):
    g = 0
    n = len(bits)
    for i in range(n):
        g += bits[i] * (2 ** (n - i - 1))

    return a + (g / (2**n - 1)) * (b - a)


def f(x, y):
    return (
        5
        + math.sin(x) * math.sin(y)
        + 0.5 * math.sin(2 * x) * math.sin(2 * y)
        - 0.1 * (x**2 + y**2)
    )


def gera_individuo(n_bits):
    s = []
    for _ in range(n_bits):
        s.append(random.randint(0, 1))
    return s


def avalia_solucao(sol):
    min_x, max_x = -8, 8
    min_y, max_y = -8, 8
    n = len(sol)
    m = n // 2

    sol_x = sol[:m]
    sol_y = sol[m:]

    x = bin_float(sol_x, min_x, max_x)
    y = bin_float(sol_y, min_y, max_y)

    return f(x, y), x, y


def selecao_torneio(populacao, k):
    competidores = random.sample(populacao, k)
    competidores.sort(key=lambda ind: ind['fitness'], reverse=True)
    return competidores[0]


def cruzamento_um_ponto(pai1, pai2, prob_cruzamento):
    if random.random() < prob_cruzamento:
        ponto_corte = random.randint(1, len(pai1['genes']) - 1)

        filho1_genes = pai1['genes'][:ponto_corte] + \
            pai2['genes'][ponto_corte:]
        filho2_genes = pai2['genes'][:ponto_corte] + \
            pai1['genes'][ponto_corte:]

        return filho1_genes, filho2_genes
    else:
        return pai1['genes'][:], pai2['genes'][:]


def mutacao_um_bit(genes, prob_mutacao):
    if random.random() < prob_mutacao:
        pos = random.randint(0, len(genes) - 1)
        genes[pos] = 1 - genes[pos]
    return genes


def algoritmo_genetico(n_bits, tam_pop, n_geracoes, p_cruzamento, p_mutacao, k_tour, n_elite):

    populacao = []
    for _ in range(tam_pop):
        genes = gera_individuo(n_bits)
        fit, x, y = avalia_solucao(genes)
        populacao.append({'genes': genes, 'fitness': fit, 'x': x, 'y': y})

    best_global = None

    for geracao in range(n_geracoes):
        nova_populacao_candidata = []

        while len(nova_populacao_candidata) < tam_pop:

            pai1 = selecao_torneio(populacao, k_tour)
            pai2 = selecao_torneio(populacao, k_tour)

            genes_f1, genes_f2 = cruzamento_um_ponto(pai1, pai2, p_cruzamento)

            genes_f1 = mutacao_um_bit(genes_f1, p_mutacao)
            genes_f2 = mutacao_um_bit(genes_f2, p_mutacao)

            fit1, x1, y1 = avalia_solucao(genes_f1)
            fit2, x2, y2 = avalia_solucao(genes_f2)

            nova_populacao_candidata.append(
                {'genes': genes_f1, 'fitness': fit1, 'x': x1, 'y': y1})
            if len(nova_populacao_candidata) < tam_pop:
                nova_populacao_candidata.append(
                    {'genes': genes_f2, 'fitness': fit2, 'x': x2, 'y': y2})

        pool_total = populacao + nova_populacao_candidata

        pool_total.sort(key=lambda ind: ind['fitness'], reverse=True)

        nova_geracao = pool_total[:n_elite]

        restantes_necessarios = tam_pop - n_elite
        pool_restante = pool_total[n_elite:]

        if restantes_necessarios > 0:
            amostra_aleatoria = random.sample(
                pool_restante, restantes_necessarios)
            nova_geracao.extend(amostra_aleatoria)

        populacao = nova_geracao

        melhor_da_geracao = pool_total[0]
        if best_global is None or melhor_da_geracao['fitness'] > best_global['fitness']:
            best_global = melhor_da_geracao

        print(
            f"Geração {geracao+1}: Melhor Fit = {melhor_da_geracao['fitness']:.5f} (x={melhor_da_geracao['x']:.2f}, y={melhor_da_geracao['y']:.2f})")

    return best_global


def main():

    N_BITS = 32
    TAM_POP = 100
    N_GERACOES = 50
    P_CRUZAMENTO = 0.8
    P_MUTACAO = 0.05
    K_TOUR = 3
    N_ELITE = 5

    melhor_solucao = algoritmo_genetico(
        N_BITS, TAM_POP, N_GERACOES, P_CRUZAMENTO, P_MUTACAO, K_TOUR, N_ELITE
    )

    print("\n----------------- Resultado Final -----------------")
    print(f"Melhor Fitness Encontrado: {melhor_solucao['fitness']}")
    print(f"X: {melhor_solucao['x']}")
    print(f"Y: {melhor_solucao['y']}\n")


main()
