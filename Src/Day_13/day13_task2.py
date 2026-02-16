# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 13:02:34 2026

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fix file path (important!)
df = pd.read_csv(r"E:\DS_AI_Internship\src\Day13\housing_data.csv")

# Scatter Plot
plt.figure()
sns.scatterplot(x=df["Area_sqft"], y=df["Price"])
plt.title("Area vs Price")
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price")
plt.show()

print("\nObservation (Scatter Plot):")
print("As Area_sqft increases, Price seems to increase.")

# Box Plot
plt.figure()
sns.boxplot(x=df["City"], y=df["Price"])
plt.title("City vs Price")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()

print("\nObservation (Box Plot):")
print("House prices vary by city. Some cities show higher median prices compared to others.")