nomes  = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom"]

nomes_com_A = list(filter(lambda nome: nome[0] == "A", nomes))

print(nomes_com_A)