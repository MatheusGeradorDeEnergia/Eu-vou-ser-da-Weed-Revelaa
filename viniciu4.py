lista1 = input("Digite os números da Lista 1 separados por espaço: ").split()
lista2 = input("Digite os números da Lista 2 separados por espaço: ").split()

lista1 = [int(num) for num in lista1]
lista2 = [int(num) for num in lista2]

lista_unificada = list(set(lista1 + lista2))

print("Lista unificada:", *lista_unificada)

