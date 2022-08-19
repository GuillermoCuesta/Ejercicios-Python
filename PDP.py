from array import array

#creacion de variables
from numpy import array

pen =0
cost=0
costEnc=0
prob=0.0
etapa=0

ante=0
actual=0

#ingreso del valor de la variables por consola
pen = int(input("ingrese la penalizacion inicial\n"))
costEnc = int(input("ingrese el costo de encendido de la maquina\n"))
cost = int(input("ingrese el costo unitario del producto\n"))
prob = float(input("ingrese el valor de la brobabilidad\n"))
etapa = int(input("ingrese el numero maximo de etapas para alcanzar a obtener el producto"))


#print("Etapa ") 
#print(etapa+1)
#print("  Penalizacion de: ")
#print(pen/100)


print("Etapa "+str(4)+"Penalizacion de: "+str(pen/100) )

x_n=0; Kx_n=costEnc; F_n=0.0

Eta= [10]
while True:
    if(x_n == 0):

        F_n = 0 + x_n + ((1/2)**x_n) * pen
        actual = F_n
        Eta.append(F_n)
        x_n=+1

    F_n = Kx_n + x_n + ((1/2)**x_n) * pen
    
    Eta.append(F_n)

    if(F_n > actual):
        break
    
    actual = F_n
    x_n=+1

for Eta in Eta:
    print(Eta)

if(Eta[x_n-2] == Eta[x_n-1]):
    print("Se deben producir " + x_n-2 + " o "+ x_n-1 + " articulos con un costo de: " + Eta[x_n-1]+" \n")
    print("Si aun no se a obtenido un articulo aceptable\n")

print("Se deben producir " + x_n-1 + " articulos con un costo de: " + Eta[x_n-1]+" \n")
print("Si aun no se a obtenido un articulo aceptable\n")

 
    
    



