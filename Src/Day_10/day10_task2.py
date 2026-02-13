# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:53:12 2026

@author: User
"""


import pandas as pd

data = {
    "Product": [
        "Apple iPhone 14",
        "Samsung Galaxy S23",
        "Dell Inspiron 15 Laptop",
        "Sony WH-1000XM5 Headphones"
    ],
    "Price": ["$799.99", "$999.50", "$650.00", "$349.99"],
    "Date": ["2024-01-05", "2024-01-10", "2024-02-01", "2024-02-05"]
}

df = pd.DataFrame(data)


print("Before Conversion:\n")
print(df.dtypes)


df["Price"] = df["Price"].str.replace("$", "", regex=False)
df["Price"] = df["Price"].astype(float)


df["Date"] = pd.to_datetime(df["Date"])



print("\nAfter Conversion:\n")
print(df.dtypes)


print("\nAverage Price:", df["Price"].mean())
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())


print("\nMonth Column:")
print(df["Date"].dt.month)
