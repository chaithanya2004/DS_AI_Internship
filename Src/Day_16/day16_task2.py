# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:47:31 2026

@author: User
"""

import pandas as pd
import numpy as np


data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G"],
    "Marks": [50, 55, 60, 65, 70, 75, 120]  
}

df = pd.DataFrame(data)

mean = df["Marks"].mean()
std = df["Marks"].std()


df["z_score"] = (df["Marks"] - mean) / std

outliers = df[abs(df["z_score"]) > 3]

print("Mean:", mean)
print("Standard Deviation:", std)
print("\nFull Data:")
print(df)

print("\nOutliers (|Z| > 3):")
print(outliers)
