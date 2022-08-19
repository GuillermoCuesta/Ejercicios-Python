import numpy as np
import matplotlib.pyplot as mpl
#Rango del eje x
x = np.arange(-10,10,0.01)
#funciones
y1 = x
y2 = 1/2 +(0 *x)
y3 = 3-2*x
#generar graficas
mpl.plot(x,y1, color="blue", label="y1 = x")
mpl.plot(x,y2, color="green", label="y2 = 1/2")
mpl.plot(x,y3, color="red", label="y3 = 3-2*x")
#titulo del grafico
mpl.title("Grafica de la funcion y=5-2x")
#plano cartesiano
mpl.axhline(0, color="black")
mpl.axvline(0, color="black")
#nombre de los ejes
mpl.xlabel("Eje x")
mpl.ylabel("Eje y")
mpl.grid()#cuadricula
mpl.legend()
mpl.show()

