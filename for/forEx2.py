x = 0
y = int(input("Digite um numero: "))

for i in range(1, (y+1)):
    if i%2 == 0:
        print(f"{x} + {i}")
        x += i


print(f"a soma de todos os numeros pares de 1 a {y} é igual a: {x}")