nota1 = int(input("Digite um número inteiro positivo: "))

a, b = 0, 1
print(a)
for i in range(1, nota1):
    print(b)
    a, b = b, a + b
