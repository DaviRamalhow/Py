quadrados = [x**2 for x  in range(10)]
print(quadrados)

quadrados = []
for x  in range(10):
    quadrados.append(x**3)
print(quadrados)

quadrados = [x**2 for x  in range(10) if x %2 == 0]
print(quadrados)
