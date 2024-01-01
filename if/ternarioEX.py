#score 50 ou menos baixa
#score menor que 80 maior que 50 media
#score maior igual 80 alta

score = int(input("Digite a score: 123"))
status = "baixa" if score < 50 else "media" if score < 80 else "alta"
print(status)