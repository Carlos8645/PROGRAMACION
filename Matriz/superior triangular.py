def matriz_triangular_superior(matriz):
    if len(matriz) != len(matriz[0]):
        print("no es cuadrada")
        return None
    matriz_triangular = [[0] * len(matriz[0]) for _ in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            matriz_triangular[i][j] = matriz[i][j]
    return matriz_triangular
#datos
filas = input("filas de la matriz: ")
columnas = input("columnas de la matriz: ")
matriz = []
print("elementos de la matriz:")
for _ in range(filas):
    fila = []
    for _ in range(columnas):
        elemento = int(input("Ingrese un elemento: "))
        fila.append(elemento)
    matriz.append(fila)

# Llamar a la función 
resultado = matriz_triangular_superior(matriz)
if resultado is not None:
    print("La matriz triangular superior es:")
    for fila in resultado:
        print(fila)
