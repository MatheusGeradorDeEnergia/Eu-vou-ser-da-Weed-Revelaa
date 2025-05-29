produtos = {}
quantidade = int(input("Quantos produtos deseja cadastrar? "))

for _ in range(quantidade):
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade em estoque: "))
    produtos[nome] = qtd

print("\nEstoque completo:")
for nome, qtd in produtos.items():
    print(f"{nome}: {qtd} unidades")

consulta = input("\nDigite o nome de um produto para consultar o estoque: ")
if consulta in produtos:
    print(f"{consulta} tem {produtos[consulta]} unidades disponiveis.")
else:
    print("Produto não cadastrado.")
