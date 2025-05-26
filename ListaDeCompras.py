compras = ["pão", "café", "leite"]
i = ""
while i != "f":
    print("Lista de compras:", compras)
    i = input('Deseja adicionar um item? Digite "s" para sim, "n" para não ou "f" para finalizar: ')
    if i == "s":
        compras.append(input("Insira o item: "))
        compras.sort()
        print("Lista de compras:", compras)
    elif i == "n":
        i = input('Deseja remover um item? Digite "s" para sim ou "n" para não: ')
        if i == "s":
            compras.remove(input("Digite o item que deseja remover: "))
            print("Lista de compras:", compras)
            