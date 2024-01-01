import random

numero_secreto = random.randint(1, 100)
tentativas = 0

#print(numero_secreto)

while True:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1
    
    if palpite < numero_secreto:
        print("O numero secreto é maior. Tente novamento!")
        
    elif palpite > numero_secreto:
        print("O numero secreto é menor. Tente novamente")
        
    else:
        print(f"ACERTOU, o numero {numero_secreto} em {tentativas} tentativas")
        break