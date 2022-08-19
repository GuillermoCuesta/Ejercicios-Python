#Librerías necesarias
import numpy as np
import matplotlib.pyplot as mpl
#Rango del eje x
x = np.arange(-10,10,0.1)
#funcion
y = (x+2)/2
#Generar grafico
mpl.plot(x,y, color="blue", label="y=(x+2)/2")
mpl.title("Grafica de la funcion y=(x+2)/2")#Titulo de la grafica 
#Plano cartesiano
mpl.axhline(0, color="black")
mpl.axvline(0, color="black")
#nombre de los ejes
mpl.xlabel("Eje x")
mpl.ylabel("Eje y")
mpl.grid()#cuadricula
mpl.legend()
mpl.show()





 

