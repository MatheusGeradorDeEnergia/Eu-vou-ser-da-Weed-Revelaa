with open("dados.txt", "w") as arq:
    nome = input("Informe seu nome: ")
    data_nasc = input("Sua data de nascimento: ")
    arq.write(f"Nome: {nome} | Data de Nascimento: {data_nasc}")

with open("dados.txt", "r") as arquivo:
    info = arquivo.read()
    print(info)