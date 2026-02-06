# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:31:04 2026

@author: User
"""
#simple code
def greet():
    print("hello")
greet()

#using parameter
def add(a,b):
    return a+b
result=add(4,5)
print(result)

#Global scope and local scope
x=10;
    
def show_value():
    x = 5
    print(x)
show_value()
print(x)


import math;

print(math.sqrt(4))

import random;
print(random.uniform(10, 20))



