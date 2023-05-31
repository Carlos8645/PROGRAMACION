def matriz_triangular_inferior(matriz):
    if len(matriz) != len(matriz[0]):
        print("no es cuadrada")
        return None
    matriz_triangular = [[0] * len(matriz[0]) for _ in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(i + 1):
            matriz_triangular[i][j] = matriz[i][j]

    return matriz_triangular
# Ingreso de datos para la matriz
filas = int(input("filas de la matriz: "))
columnas = int(input("columnas de la matriz: "))
matriz = []
print("elementos de la matriz: ")
for _ in range(filas):
    fila = []
    for _ in range(columnas):
        elemento = int(input("Ingrese un elemento: "))
        fila.append(elemento)
    matriz.append(fila)
resultado = matriz_triangular_inferior(matriz)
if resultado is not None:
    print("La matriz triangular inferior es:")
    for fila in resultado:
        print(fila)
