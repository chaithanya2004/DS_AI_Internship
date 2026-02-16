# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:53:14 2026

@author: User
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"E:\DS_AI_Internship\src\Day13\housing_data.csv")


corr_matrix = df.corr(numeric_only=True)
print("Correlation Matrix:\n")
print(corr_matrix)


plt.figure()
sns.heatmap(corr_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.show()


print("\nHighly Correlated Pairs (> 0.8):\n")

for col1 in corr_matrix.columns:
    for col2 in corr_matrix.columns:
        if col1 != col2 and abs(corr_matrix.loc[col1, col2]) > 0.8:
            print(col1, "and", col2, "=", corr_matrix.loc[col1, col2])


plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot for Price (Outlier Detection)")
plt.show()