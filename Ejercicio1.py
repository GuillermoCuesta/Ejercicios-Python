#Librerías necesarias
import numpy as np
import matplotlib.pyplot as mpl
#Rango del eje x
x = np.arange(-10,10,0.01)

#funcion
y = 5-2*x

#Generar grafico
mpl.plot(x,y, color="blue", label="y=5-2x")
mpl.title("Grafica de la funcion y=5-2x")#Titulo de la grafica 
#Plano cartesiano
mpl.axhline(0, color="black")
mpl.axvline(0, color="black")
#nombre de los ejes 
mpl.xlabel("Eje x")
mpl.ylabel("Eje y")
mpl.grid()#cuadricula
mpl.legend()
mpl.show()

