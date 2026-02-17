# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:32:39 2026

@author: User
"""

# Import required libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\n")


le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print("After Label Encoding (Transmission):")
print(df)
print("\n")

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("After One-Hot Encoding (Color) with drop_first=True:")
print(df)