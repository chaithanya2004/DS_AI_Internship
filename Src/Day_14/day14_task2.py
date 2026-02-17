# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:28:42 2026

@author: User
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


data = {
    "Salary": [10000, 15000, 20000, 25000, 30000, 50000, 100000, 200000, 500000]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)
print("\n")


scaler = StandardScaler()
df["Standardized"] = scaler.fit_transform(df[["Salary"]])


df["Log_Salary"] = np.log(df["Salary"])

print("Transformed Data:\n")
print(df)
print("\n")



plt.figure()
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df["Standardized"], bins=5)
plt.title("Standardized Salary Distribution")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df["Log_Salary"], bins=5)
plt.title("Log Transformed Salary Distribution")
plt.xlabel("Log Salary")
plt.ylabel("Frequency")
plt.show()