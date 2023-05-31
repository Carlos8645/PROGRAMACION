#Escriba un programa para hacer un patrón como un triángulo rectángulo con un número que repetirá un número seguido.
l=1
v=0
while v < 6:
    v=v+1
    for i in range(v):
        print(v,end="")
    print("")