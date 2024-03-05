def somar (a, b):
    """Função que retorna a soma de dois numeros.

    Args:
        a (int ou float): Primeiro numero.
        b (int ou float): Segundo numero.

    Returns:
        int ou float: A soma de a e b.
    """
    return a+b

print(somar.__doc__)
print(somar(2,3))