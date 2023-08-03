    """Busqueda binaria
        Solo funciona cuando nuestro conjunto esta ordenado
    """
def raiz_cuadrada():
    print('Vamos a hallar la raiz cuadrada de un numero entero')
    objetivo = int(input('Ingresa un numero entero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
    
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

if __name__ == '__main__':
    raiz_cuadrada()