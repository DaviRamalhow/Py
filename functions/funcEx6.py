def exbir_info(**kwargs):
    
    """Função que exibe informações pessoais"""
    for chave, valor in kwargs.items():
        print(chave + ": " + str(valor))
        
exbir_info(nome="João", idade=25, cidade="São Paulo", sexo="Masculino")
