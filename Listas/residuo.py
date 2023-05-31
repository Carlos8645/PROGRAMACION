#Residuo de una division
D=int(input("Digite un numero "))
while D>10:
    Cociente=D//10
    Residuo=D%10
    D=Cociente
    print(Residuo)
print(Cociente)