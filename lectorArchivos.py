from numpy import array


f = open("sat43204.txt") 
o = open("guardar.txt", "w")
mostrar = f.readlines()

for i in range(0,5580,2):
    linea1 = mostrar[i]
    linea2 = mostrar[i+1] 
    lineanew = linea1[1 :-1] +' '+ linea2[1:]

    print(lineanew)
    
    o.writelines(lineanew) 

f.close()
o.close()