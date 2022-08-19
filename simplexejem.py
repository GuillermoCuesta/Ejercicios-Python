#Paquete de importación
from scipy import optimize
import numpy as np
import matplotlib as plt
#OK c, A_ub, B_ub
#constantes de la funcion objetivo
c = np.array([3,-2]) 
#valores correspondientes a las variables de las restriciones 
A_ub = np.array([[2,1],[2,3],[3,-2]]) 
# valores de las restrcciones
B_ub = np.array([18,42,5]) 
#Resolver
res =optimize.linprog(c,A_ub,B_ub)
print(res)
