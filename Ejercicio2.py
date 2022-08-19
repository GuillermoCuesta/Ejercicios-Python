#Librerías necesarias
import numpy as np
import matplotlib.pyplot as mpl
#Rango del eje x y y
x = np.arange(-50,50,0.01)
y = np.arange(-2, 100, 0.01)
#funcion
y = 5 + (0 * x)
#Generar grafico
mpl.plot(x,y, color="blue", label="y=5")
mpl.title("Grafica de la funcion y=5")#Titulo de la grafica 
#Plano cartesiano
mpl.axhline(0, color="black")
mpl.axvline(0, color="black")
#nombre de los ejes 
mpl.xlabel("Eje x")
mpl.ylabel("Eje y")
mpl.grid()#cuadricula
mpl.legend()
mpl.show()