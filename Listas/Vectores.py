#dos vectores representados como listas
vector1 = [4, 2, 3]
vector2 = [4, 5, 7]

if len(vector1) != len(vector2):
    print("los vectores no tienen la misma longitud")
else:
    producto_punto = 0
    for i in range(len(vector1)):
        producto_punto += vector1[i] * vector2[i]
print("El producto es:", producto_punto)
