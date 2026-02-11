# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:38:52 2026

@author: User
"""
import pandas as pd;
grades=pd.Series([85, None, 92, 45, None, 78, 55]);
print("Original series:",grades)
print(grades.isnull());
print("Filled series");
new_one=grades.fillna(0);
print(new_one)
print("Filterd series")
passed = new_one[new_one> 60]
print(passed)