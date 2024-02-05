palavras = []

for i in range (1,5):
    palavras.append(input("Digite uma palavra: "))

for palavra in palavras:
    if len(palavra) > 4:
        print(palavra)
    