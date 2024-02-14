def adicionar(n1,n2):
    
    return n1+n2

def subtrair(n1,n2):
    
    return n1-n2

def multiplicar(n1,n2):
    
    return n1*n2

def dividir(n1,n2):
    
    return n1/n2


n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))


op = input("Escolha uma operação (adicionar, subtrair, multiplicar e dividir): ")

if op == "adicionar":
    
    resultado = adicionar(n1,n2)
elif op == "subtrair":
    
    resultado = subtrair(n1,n2)
elif op == "multiplicar":
    
    resultado = multiplicar(n1,n2)
elif op == "dividir":
    
    resultado = dividir(n1,n2)
else: 
    print("Operação invalida")
    
print("Resultado: ", resultado)