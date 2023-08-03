def factorial(n):
    """Calcula factorial de n

    Args:
        n (int): n > 0
        returns n!
    """
    if n == 1:
        return 1
    
    return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input('Escribe un numero entero: '))
    resultado = factorial(n)
    print(resultado)