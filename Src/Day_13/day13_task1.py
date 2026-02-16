# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:14:37 2026

@author: User
"""

import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

df=pd.read_csv("E:\DS_AI_Internship\src\Day13\housing_data.csv");
plt.figure();
sns.histplot(df["Price"],kde=True);
plt.title("House price distribution");
plt.xlabel("Price");
plt.ylabel("Frequency");
plt.show()

print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())

plt.figure()
sns.countplot(x=df["City"])
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()
