catalogo = {}
quantidade = int (input("Quantos filmes voce deseja adicionar ao catalogo? "))

for _ in range(quantidade):
    titulo = input("Titulo do filme : ")
    ano = int(input("Ano de lançamento: "))
    catalogo[titulo] = ano

print("\nCatalogo de filmes: ")
for titulo, ano in catalogo.items():
    print(f"{titulo} : {ano} ")

consultarfilme = input("Digite o nome do filme que deseja para consultar o ano de lançamento: ")
if consultarfilme in catalogo:
    print(f"o filme {consultarfilme} foi lançado em {catalogo[consultarfilme]}")

else:
    print("Esse filme nao está cadastrado no catalogo. ")
