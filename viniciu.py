entrada = input("Digite uma lista de números : ")
numeros = list(map(int, entrada.split()))
maior_numero = max(numeros)
menor_numero = min(numeros)
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
