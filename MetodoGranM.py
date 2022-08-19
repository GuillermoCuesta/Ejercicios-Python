#Paquete de importación
from scipy import optimize
import numpy as np
import matplotlib as plt
#OK c, A_ub, B_ub
#constantes de la funcion objetivo
c = np.array([-2,-4]) 
#valores correspondientes a las variables de las restriciones 
A_ub = np.array([[-2,2],[2,1],[2,3]]) 
# valores de las restrcciones
B_ub = np.array([4,9,11]) 
#Resolver
res =optimize.linprog(c,A_ub,B_ub)
print(res)