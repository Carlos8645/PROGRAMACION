lista = [3, 8, 2, 10, 5, 1]
listao = sorted(lista_numeros)
cantidad = len(listao)

if cantidad % 2 == 0:
    mediana = (listao[cantidad//2-1] + listao[cantidad//2]) / 2
else:
    mediana = listao[cantidad//2]

print("La mediana es:", mediana)



