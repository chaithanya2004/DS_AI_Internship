# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:20:43 2026

@author: User
"""
import numpy as np;
arr = np.arange(24);
print("original");
print(arr);
print("reshaped");
reshaped = arr.reshape(4,3,2)
print(reshaped);
tp=reshaped.transpose(0,2,1)
print("Final Shape:", tp.shape)
print("Transpose");
print(tp);