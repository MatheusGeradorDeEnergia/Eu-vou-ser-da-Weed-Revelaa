n = int(input("Digite um numero inteiro que seja positivo: "))
fatorial = 1

while n > 1:
    fatorial *= n
    n -= 1

print(f"O fatorial é {fatorial}")