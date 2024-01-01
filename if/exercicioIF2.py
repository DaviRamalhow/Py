#acima 1K - 20% , de 500 a 1K 10, abaixo de 500 nn tem

n = float(input("Quer saber se sua compra teve desconto?"))

if (n > 1000):
    print("vc recebe 20% de desconto")
    desconto = n * 0.20
    print(f"{desconto} reais de desconto")
    print(f"VALOR FINAL: R${n - desconto}")
    
elif(n > 500 and n < 1000):
    print("vc recebe 10% de desconto")
    desconto = n * 0.10
    print(f"{desconto} reais de desconto")
    print(f"VALOR FINAL: R${n - desconto}")
    
else:
    print("vc nn recebe desconto")