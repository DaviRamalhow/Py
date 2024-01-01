senha = int(input("Digite sua senha numerica: "))
s = 0

while s != senha:
    s1 = int(input("Digite sua senha: "))
    s = s1
    if s != senha:
        print("senha errada")
else:
    print("SENHA CORRETA")