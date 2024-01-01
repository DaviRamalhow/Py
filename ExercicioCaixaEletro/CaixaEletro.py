import time

saldo = 1000.00


while True:
        print(" ")
        print("Caixa Eletrônico")
        print("1  - Verificar saldo")
        print("2  - Depositar dinheiro")
        print("3  - Sacar dinheiro")
        print("4  - Sair")
        print("  ")
        
        opts = int(input("Escolha uma opção (1-4):"))
        
        if opts == 1:
            print(f"seu saldo é de: R${saldo}")
            time.sleep(2)
            
        elif opts == 2:
            deposito = int(input("Digite o valor do depósito: "))
            
            if deposito <= 0:
                print("Ops, valor invalido. Realize a operação novamente!")
            else:
                saldo += deposito
                print("Depósito realizado com sucesso")
                
            time.sleep(2)
            
        elif opts == 3:
            saque = int(input("Digite o valor do saque: "))
            if saque > saldo:
                print("Ops, parece que vc tentou sacar um valor maior que seu saldo.")
                print("Realize a operação novamente!")
            else:
                saldo -= saque
                print("Saque realizado com sucesso")
            time.sleep(2)
            
        elif opts == 4:
            break
        
        else:
            print("Opção invalida")
            time.sleep(2)