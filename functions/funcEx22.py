def contar_regressivamente(n):

    if n > 0:
        print(n)
        contar_regressivamente(n-1)
        
contar_regressivamente(5)