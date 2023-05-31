lista= [3, 8, 2, 10, 5, 1]
cantidad = len(lista)
suma= sum(lista)
media = suma/ cantidad

varianza = sum([(x - media)**2 for x in lista]) / (cantidad - 1)

print("La varianza es:", varianza)





