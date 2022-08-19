#Librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

#Ecuaciones e intervalos (Para tabular)
x = np.arange(-20, 150, 20)
y = np.arange(0, 150, 5)
y1 = (3000 - (60 * x))/ 24
x1 = 23+(0 * y)
y3 = 20 + (0 * x)
y4 = 65 - x
z = (-120 * x) / 200


#Graficando las líneas
plt.plot(x, y1, '-', linewidth=2, color='b')
#plt.plot(x, y2, '-', linewidth=2, color='g')
plt.plot(x, y3, '-', linewidth=2, color='r')
plt.plot(x1, y, '-', linewidth=2, color='y')
plt.plot(x, y4, '-', linewidth=2, color='k')
plt.plot(x, z, ':', linewidth=1, color='g')

#Configuraciones adicionales del gráfico
plt.grid()
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title('Método Gráfico')



plt.show()