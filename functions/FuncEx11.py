def nivel_saudacao(nivel):
    
    def saudacao_basica():
        return "Oi!"
    
    def saudacao_avancada():
        return "Olá, como voce esta?"
    
    if nivel == "basica":
        return saudacao_basica
    else:
        return saudacao_avancada
    

cumprimento = nivel_saudacao("")
print(cumprimento())