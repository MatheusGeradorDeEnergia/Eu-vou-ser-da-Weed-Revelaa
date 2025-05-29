projetos = []

while True:
    if input("Deseja cadastrar um projeto? (s/n): ") != "s":
        break
    nome = input("Nome do projeto: ")
    responsavel = input("Nome do responsável: ")
    horas = int(input("Horas estimadas: "))
    status = input("Status (ativo/finalizado): ")
    projetos.append([nome, responsavel, horas, status])

while True:
    print("\n1 - Listar projetos\n2 - Buscar por responsável\n3 - Projetos ativos\n4 - Somar horas\n5 - Mudar status\n6 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        for p in projetos:
            print(f"Nome: {p[0]} - Responsável: {p[1]} - Horas: {p[2]} - Status: {p[3]}")
    elif escolha == "2":
        resp = input("Digite o nome do responsável: ")
        for p in projetos:
            if p[1] == resp:
                print(f"Nome: {p[0]} - Horas: {p[2]} - Status: {p[3]}")
    elif escolha == "3":
        for p in projetos:
            if p[3] == "ativo":
                print(f"Nome: {p[0]} - Responsável: {p[1]} - Horas: {p[2]}")
    elif escolha == "4":
        print("Total de horas:", sum(p[2] for p in projetos))
    elif escolha == "5":
        nome = input("Nome do projeto para mudar o status: ")
        for p in projetos:
            if p[0] == nome:
                p[3] = "finalizado" if p[3] == "ativo" else "ativo"
                print("Status alterado!")
                break
    elif escolha == "6":
        print("Saindo...")
        break
