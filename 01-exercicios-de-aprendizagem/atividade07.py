frutas = set()
repetidas = 0

try:
    print("Cadastro de Frutas")

    while True:
        fruta = input("Digite o nome da fruta: ")
        if fruta.lower() == "sair":
            print("Cadastro finalizado.")
            break
        if fruta in frutas:
            repetidas += 1
            print(f"A fruta '{fruta}' já foi cadastrada.")
        else:
            frutas.add(fruta)
            print(f"A fruta '{fruta}' foi cadastrada com sucesso.")

    print("\nFrutas cadastradas:")

    for fruta in frutas:
        print(fruta)

    print(f"Total de frutas repetidas: {repetidas}")
except Exception as _:
    print("Programa finalizado.")
