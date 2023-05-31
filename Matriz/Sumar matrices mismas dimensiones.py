def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("no tienen las mismas dimensiones")
        return None
    resultado = [[0] * len(matriz1[0]) for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return resultado
filas1 = int(input("Ingrese el numero de filas de la matriz 1:"))
columnas1 = int(input("Ingrese el numero de columnas de la matriz 1:"))
matriz1 = []
print("Ingrese los elementos de la matriz 1:")
for _ in range(filas1):
    fila = []
    for _ in range(columnas1):
        elemento = int(input("Ingrese un elemento: "))
        fila.append(elemento)
    matriz1.append(fila)
filas2 = int(input("Ingrese el número de filas de la matriz 2: "))
columnas2 = int(input("Ingrese el número de columnas de la matriz 2: "))

matriz2 = []
print("Ingrese los elementos de la matriz 2:")
for _ in range(filas2):
    fila = []
    for _ in range(columnas2):
        elemento = int(input("Ingrese un elemento: "))
        fila.append(elemento)
    matriz2.append(fila)
##Llamar a la funcion sumar_matrices y mostrar el resultado
resultado = sumar_matrices(matriz1, matriz2)
if resultado is not None:
    print("El resultado de la suma de matrices es:")
    for fila in resultado:
        print(fila)

