n1 = 7
n2 =3

tries = 5

guess = False
guess2 = False

while tries > 0 and (not guess or not guess2):
    print(f"Tentivas restantes: {tries}")
    
    tri = int(input("Adivinhe o primeiro numero secreto (1-10): "))
    tri2 = int(input("Adivinhe o segundo numero secreto (1-10): "))
    
    if tri == n1:
        print("Voce acertou o primeiro numero!!")
        
        guess = True
        
    if tri2 == n2:
        print("Voce acertou o segundo numero!!")
        
        guess2 = True
        
    if not guess or not guess2:
        print("tente novamente")
        
        tries -=1
        
if guess == True and guess2 == True:
    print("parabens, adivinhou os dois numeros")
    
else:
    print(f"Vc errou< os numeros eram: n1: {n1}, n2: {n2}")