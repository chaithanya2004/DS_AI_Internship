# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 11:14:19 2026

@author: User
"""

# STEP 1 — Import pandas
import pandas as pd

# STEP 1 — Load the dataset
df = pd.read_csv("E:\DS_AI_Internship\src\Day10\customer_orders.csv")
print("Shape before cleaning:", df.shape)
print("\nMissing values per column:")
print(df.isna().sum())
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())
    
df = df.drop_duplicates()

print("\nShape after cleaning:", df.shape)
