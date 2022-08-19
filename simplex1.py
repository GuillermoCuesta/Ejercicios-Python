import numpy as np
def pivot(d,bn):
    l = list(d[0][:-2])
    jnum = l.index(max(l)) # Transferir número
    m = []
    for i in range(bn):
        if d[i][jnum] == 0:
            m.append(0.)
        else:
            m.append(d[i][-1]/d[i][jnum])
    inum = m.index(min([x for x in m[1:] if x!=0]))  # Transferir subíndice
    s[inum-1] = jnum
    r = d[inum][jnum]
    d[inum] /= r
    for i in [x for x in range(bn) if x !=inum]:
        r = d[i][jnum]
        d[i] -= r * d[inum]        
def solve(d,bn):
    flag = True
    while flag:
        if max(list(d[0][:-1])) <= 0: #Hasta que todos los coeficientes sean menores o iguales a 0
            flag = False
        else:
            pivot(d,bn)            
def printSol(d,cn):
    for i in range(cn - 1):
        if i in s:
            print("x"+str(i)+"=%.2f" % d[s.index(i)+1][-1])
        else:
            print("x"+str(i)+"=0.00")
    print("objective is %.2f"%(-d[0][-1]))
d = np.loadtxt("D:\\my.txt", dtype=np.float)
(bn,cn) = d.shape
s = list(range(cn-bn,cn-1)) #Lista de variables #Base
solve(d,bn)
printSol(d,cn)
