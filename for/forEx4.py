x = int(input("digite um numero inteiro: "))
quad = 0

for i in range (1,x+1):
    quad += i * i
    print(f"quadrado de {i} é: {i* i}")

print(f"soma dos quadrados de 1 até {x} é: {quad}")