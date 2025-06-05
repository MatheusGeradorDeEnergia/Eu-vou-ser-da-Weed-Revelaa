produtos = []

while True:
    print("1. Cadastrar produtos")
    print("2. Listar produtos")
    print("3. Buscar produto pelo nome")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produtos.append({"nome": nome, "preco": preco})
    elif opcao == "2":
        for produto in produtos:
            print(f"Nome: {produto['nome']} | Preço: {produto['preco']}")
    elif opcao == "3":
        busca = input("Digite o nome do produto para buscar: ")
        encontrado = False
        for produto in produtos:
            if produto["nome"].lower() == busca.lower():
                print(f"Produto encontrado: {produto['nome']} | Preço: {produto['preco']}")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")
