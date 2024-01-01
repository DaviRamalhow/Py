n = 0

while True:
    n1 = int(input("Digite um numero inteiro maior que zero: "))
    if n1> n:
        n = n1
    elif n1 < 0:
        print(f"O maior numero foi {n}")
        break
    
    n1 = 0
    