#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
from array import *
import pylab

# punkty
n = 6
h = 1
tabX = [0,1,2,3,4,5]
tabY = [3,7,1,1,5,9]

#T = np.matrix[[n-2],[n-2]]
T = [[0.0] * (n-2) for i in range(n-2)]
print(T)

for i in range (0,n-2):
    print(i)
    arr = [0] * (n-2)
    #print(arr)
    #for x in range (1,n-2):
        #arr.append(0)
        
    #diagonala
    arr[i] = 4.0
    #print(arr)
    
    #nad diagonalą
    if (i > n-4):
        pass
    else:
        arr[i+1] = 1.0
    
    #pod diagonalą
    if (i < 1):
        pass
    else:
        arr[i-1] = 1.0
    
    print(arr)
    #M.insert[]
    
    T[i] = arr
    print(T)

print("")
T2 = np.linalg.inv(T)
print(T2)

print("")
#Y = [[0 for c in range (1)] for r in range (n-2)]
Y = [0.0] * (n-2)
print(Y)

for i in range (0, n-2):
    h = tabX[i+1] - tabX[i]
    Y[i] = int(tabY[i] - 2*tabY[i+1] + tabY[i+2]) * (6.0 / (h**2))
print(Y)

print("")
Y2 = [0.0] * (n-2)
mult = 0.0
for i in range (0, n-2):
    mult = 0.0
    for j in range (0, n-2):
        mult += Y[j] * T2[i][j]
        #print(Y[j],T2[i][j])
    Y2[i] = mult
print(Y2)

print("")
M = [0.0] * n
for i in range (1,n-1):
    M[i] = Y2[i-1]
print(M)

print("")
A = [0.0] * (n-1)
B = [0.0] * (n-1)
C = [0.0] * (n-1)
D = [0.0] * (n-1)
for i in range (0, n-1):
    A[i] = (M[i+1] - M[i]) / (6.0 * (tabX[i+1] - tabX[i]))
    B[i] = M[i] / 2.0
    C[i] = ((tabY[i+1] - tabY[i]) / (tabX[i+1] - tabX[i])) - (((M[i+1] + (2 * M[i])) / 6.0) * (tabX[i+1] - tabX[i]))
    D[i] = tabY[i]
    
print(A)
print(B)
print(C)
print(D)

print("")
rr = np.arange(-5, 5, 0.1)

def y(o):
    i = 0
    return (A[i] * ((o - tabX[i])**3)) + (B[i] * ((o - tabX[i])**2)) + (C[i] * (o - tabX[i])) + D[i]

plt.plot(rr, y(rr).astype(np.int))
plt.show()

def y2(o):
    i = 1
    return (A[i] * ((o - tabX[i])**3)) + (B[i] * ((o - tabX[i])**2)) + (C[i] * (o - tabX[i])) + D[i]

def y3(o):
    i = 2
    return (A[i] * ((o - tabX[i])**3)) + (B[i] * ((o - tabX[i])**2)) + (C[i] * (o - tabX[i])) + D[i]

plt.plot(rr, y(rr).astype(np.int))
plt.plot(rr, y2(rr).astype(np.int))
plt.plot(rr, y3(rr).astype(np.int))
plt.show()

'''
for i in range (0, n-1):
    y = [(A[i] * ((i - tabX[i])**3)) + (B[i] * ((i - tabX[i])**2)) + (C[i] * (i - tabX[i])) + D[i] for i in x]
    print(x, len(x))
    print(y, len(y))
    pylab.plot(x, y)
    pylab.grid(True)
    pylab.show()
'''
print("koniec")
    
    


# In[ ]:




