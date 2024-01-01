n = 0

while True:
    n1 = int(input("Digite um numero inteiro (0 para sair): "))
    n += n1
    if n1 == 0:
        print(f"A soma de todos os numeros digitados é {n}")
        break

    n1 = 0
    