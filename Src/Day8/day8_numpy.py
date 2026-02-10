# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 10:34:34 2026

@author: User
"""


import numpy as np;
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)
print("1D");
a1=np.array([1,2,3]);
print(a1);
print("OD")
a0=np.array([7]);
print(a0);
print("3D")
a3=np.array([[4,5,6],[8,9,10],[9,10,23]]);
print(a3);


arr = np.random.rand(100000)
squared = arr ** 2
print(arr)
print(squared);

arr = np.random.randint(100)
squared = arr ** 2
print(arr)
print(squared);

#reshapeing
print("Reshape");
arr = np.arange(12)#o to 11 numbers
reshaped = arr.reshape(3, 4)
print(reshaped)

#vertical stack
print("vertical stack")
a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)

#hstack
print("Horigontal stack")
a = np.array([[1, 2]])
b = np.array([[3, 4]])

hstacked = np.hstack((a, b))
print(hstacked)


data = np.array([[10, 20, 30],   #it calculates the avaerage of 
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data, axis=1))



A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(np.dot(A, B))

print(np.invert(A,B))


#LINESPACE

arr=np.linspace(0,3,4);
print(arr)

#random.rand
arr2=np.random.uniform(100)
print(arr2)


