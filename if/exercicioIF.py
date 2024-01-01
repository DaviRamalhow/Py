# n1 = 50
# n2 = 21
# n3 =200

# if n1 > n2 and n3 > n1:
#     print("As duas são verdade")
# else:
#     print("n")

#70-89 bom 90-100-excelnte

nota = int(input("Digite uma nota de 1 a 100:"))

if(nota <= 49):
    print("nota insuficiente")
    
elif(nota >= 50 and nota < 69):
    print("nota satisfatória")
elif(nota >=70 and nota <=89):
    print("Nota boa")
else:
    print("Excelente")