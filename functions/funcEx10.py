def saudacao_nome(nome):
    
    return f"Olá, {nome}"

def cumprimentar(func, nome):
    
    return func(nome)


print(cumprimentar(saudacao_nome, "Ana"))