# n1 = 19
# n2 = 150
# n3 = 18

# if n1 > n2 or n1 > n3:
#     print(f"O {n1} é maior que {n2} ou {n1} é maior que {n3}")

#Exewmplo, tem que atender pelo menos uma das condições para entrar em um evento exclusivo
print(" RESPONDA TODAS AS PERGUNTAS COM SIM OU NÃO")

p1 = input("Vc tem um convite VIP?")

p2 = input("Vc esta na lista de convidados?")

p3 = input("Vc é membro do clube?")

if (p1 == "sim" or p2 == "sim" or p3 == "sim"):
    print("pode entrar")
else:
    print("Voce não poderá entrar no evento")
