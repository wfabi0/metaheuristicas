paisA = 80000
taxa_anualA = 0.03

paisB = 200000
taxa_anualB = 0.015

anos = 0
while paisA < paisB:
    paisA += paisA * taxa_anualA
    paisB += paisB * taxa_anualB
    print(f"Ano {anos + 1}:")
    print(f"População do País A: {int(paisA)}")
    print(f"População do País B: {int(paisB)}")
    print()
    anos += 1

print(f"A população do País A ultrapassou ou igualou a do País B em {anos} anos.")