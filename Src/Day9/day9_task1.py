# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:22:39 2026

@author: User
"""

import pandas as pd;
series=pd.Series([ 700, 150, 300], index=['laptop', 'Mouse', 'Keyboard'])
print("Full series:",series)
print("First index value:",series['laptop'])
print("first 2 values in the series")
slice=series[0:2];
print(slice)