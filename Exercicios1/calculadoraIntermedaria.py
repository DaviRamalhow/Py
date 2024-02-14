def calculadora(op):
    
    def adicionar(*n):
        total = n
        for x in n:
            total+=x
        return total

    def subtrair(*n):
        total = n[0]
        for x in n[1:]:
            total-=x
        return total

    def multiplicar(*n):
        total = 1
        for x in n:
            total*=x
        return total

    def dividir(*n):
        total = n[0]
        for x in n[1:]:
            total/=x
        return total
    
    def invalida():
        
        return "Operação invalida"
    
    if op == "adicionar":
        return adicionar
    
    elif op == "subtrair":
        return subtrair
    
    elif op == "multiplicar":
        return multiplicar
    
    elif op == "dividir":
        return dividir
    else:
        return invalida
    
    

numeros = input("Digite quantos numeros vc quiser separados por espaços: ").split()
numeros = [float(x) for x in numeros]

oper = input("Escolha uma operação (adicionar, subtrair, multiplicar e dividir): ")

calc = calculadora(oper)
print(calc(*numeros))
