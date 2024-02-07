def estatistica(*n):
    
    return sum(n)/len(n), max(n), min(n)

nList = list(map(float, input("Digite uma sequencia numerica separada por espaços").split()))

media, maior, menor= estatistica(*nList)
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")