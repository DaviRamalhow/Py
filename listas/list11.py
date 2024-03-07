minha_lista = [0,1,2,3,4,5,6,7,8,9]
subconjunto = minha_lista[1:4]

print(subconjunto)

priemiros_elementos = minha_lista[:2]
print(priemiros_elementos)

elementos_depois_do2 = minha_lista[2:]
print(elementos_depois_do2)


elementos_alternados = minha_lista[::2]#Mostra de 2 em 2, se colocar 3 vai de 3 em 3 e assim por diante
print(elementos_alternados)

#se Usar por exemplo minha_lista[2:8:2]
# Ele começa no indice 2 e vai até 8(n inclui o 8) de 2 em 2