def multi_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("Error: las matrices no son multiplicables")
        return None
    resultado = [[0] * len(matriz2[0]) for _ in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado
#datos para la matriz1
filas1 = int(input("numero de filas de la matriz 1: "))
columnas1 = int(input("numero de columnas de la matriz 1: "))
matriz1 = []
print("Ingrese los numeros de la matriz 1:")
for _ in range(filas1):
    fila = []
    for _ in range(columnas1):
        elemento = int(input("Ingrese un elemento: "))
        fila.append(elemento)
    matriz1.append(fila)
#datos para la matriz2
filas2 = int(input("numero de filas de la matriz 2: "))
columnas2 = int(input("numero de columnas de la matriz 2: "))
matriz2 = []
print("Ingrese los elementos de la matriz 2:")
for _ in range(filas2):
    fila = []
    for _ in range(columnas2):
        elemento = int(input("Ingrese un elemento: "))
        fila.append(elemento)
    matriz2.append(fila)

#funcion
resultado = multi_matrices(matriz1, matriz2)
if resultado is not None:
    print("El resultado es:")
    for fila in resultado:
        print(fila)
