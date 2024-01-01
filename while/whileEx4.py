n = 1

max = int(input("Digite um inteiro maior que 1: "))

print(f"Numeros pares entre 1 e {max}:")

while n <= max:
    if n %2 == 0:
        print(n, end=" ")
    n+=1
