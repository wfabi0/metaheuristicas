idade = int(input("Insira sua idade: "))

valor_ingresso = 21.00

if idade < 12 or idade > 60:
    valor_ingresso *= 0.5

print(f"O valor do ingresso é: R$ {valor_ingresso:.2f}")
