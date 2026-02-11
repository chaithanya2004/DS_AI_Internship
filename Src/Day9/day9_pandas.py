# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:32:17 2026

@author: User
"""

import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)

#indexing 
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math','Chemistry']]);

#boolean masking
scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)

#handling missing data
data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(6))

#vectorization in string 
names = pd.Series(['Alice', 'bob', 'CHARLIE','alise'])

print(names.str.lower())
print(names.str.contains('a'))
print()
