def obtener_cofactor(matriz, i, j):
    if len(matriz) != len(matriz[0]):
        print("Error")
        return None
    if i < 0 or i >= len(matriz) or j < 0 or j >= len(matriz[0]):
        print("Revisar posicion")
        return None
    submatriz = [fila[:j] + fila[j+1:] for fila in (matriz[:i] + matriz[i+1:])]
    cofactor = determinante(submatriz) * (-1)**(i+j)
    return cofactor
def determinante(matriz):
    if len(matriz) == 1 and len(matriz[0]) == 1:
        return matriz[0][0]
    if len(matriz) == 2 and len(matriz[0]) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    det = 0
    for j in range(len(matriz[0])):
        det += matriz[0][j] * obtener_cofactor(matriz, 0, j)

    return det
filas = int(input("numero de filas de la matriz: "))
columnas = int(input("numero de columnas de la matriz: "))

matriz = []
print("Ingrese los elementos de la matriz:")

for _ in range(filas):
    fila = []
    for _ in range(columnas):
        elemento = int(input("Ingrese un elemento: "))
        fila.append(elemento)
    matriz.append(fila)

i = int(input("Ingrese la posicion i: "))
j = int(input("Ingrese la posicion j: "))

cofactor = obtener_cofactor(matriz, i, j)
if cofactor is not None:
    print("El cofactor en la posicion ({}, {}) es: {}".format(i, j, cofactor))
