import time
x = 0
y = 0

while True:

    print(" ")
    print("CALCULADORA")
    print("1 - somar")
    print("2 - subtrair")
    print("3 - mulplicar")
    print("4 - dividir")
    print("5 - sair")
    print(" ")
    op = int(input("Escolha a opéração que deseja realizar: (1-5):"))
    
    if op == 1:
        print("Escolha os dois numeros que vc quer somar: ")
        x = float(input("numero 1: "))
        y = float(input("numero 2: "))
        soma = x + y
        print(f"o resultado da soma é: {soma}")
        time.sleep(2)
        
    elif op == 2:
        print("Escolha os dois numeros que vc quer subtrair: ")
        x = float(input("numero 1: "))
        y = float(input("numero 2: "))
        sub = x - y
        print(f"o resultado da subtração é: {sub}")
        time.sleep(2)
        
    elif op == 3:
        print("Escolha os dois numeros que vc quer multiplicar: ")
        x = float(input("numero 1: "))
        y = float(input("numero 2: "))
        mult = x * y
        print(f"o resultado da multiplicação é: {mult}")
        time.sleep(2)
        
    elif op == 4:
        print("Escolha os dois numeros que vc quer dividir: ")
        x = float(input("numero 1: "))
        y = float(input("numero 2: "))
        div = x / y
        print(f"o resultado da divisão é: {div}")
        time.sleep(2)
    
    elif op == 5:
        print("Obg por usar a calculador")
        time.sleep(2)
        break
    
    else:
        print("operação invalida, tente novamente")
        time.sleep(2)