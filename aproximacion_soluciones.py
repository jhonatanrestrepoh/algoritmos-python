def raiz_cuadrada():
    print('Vamos a hallar la raiz cuadrada aproximada de un numero entero')
    objetivo = int(input('Ingresa un numero entero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada del {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

if __name__ == '__main__':
    raiz_cuadrada()