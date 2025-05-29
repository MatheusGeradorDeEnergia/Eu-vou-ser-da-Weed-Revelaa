alunos = {}
quantidade = int(input("Quantos alunos voce quer cadastrar? "))

for i in range(quantidade):
    nome = input("Nome do aluno: ")
    nota = float(input("Digite a nota entre (0 e 10): "))
    alunos[nome] = nota

print("\nLista de alunos e notas: ")
for nome, nota in alunos.items():
    print(f"{nome} : {nota} ")

consultarnota = input("\nDigite o nome de um aluno para consultar a nota: ")
if consultarnota in alunos:
    print(f"{consultarnota} teve nota {alunos[consultarnota]} ")
else:
    print("Aluno nao cadastrado ")
