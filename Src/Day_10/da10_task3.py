# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 13:00:25 2026

@author: User
"""

import pandas as pd

# Sample data
data = {
    'Location': [' New York', 'new york', 'NEW YORK ', 'Los Angeles', 'los angeles ']
}

# Create DataFrame
df = pd.DataFrame(data)

print("Before normalization:")
print(df)

# Normalize Location column
df['Location'] = df['Location'].str.strip().str.title()  # Remove spaces and standardize casing

print("\nAfter normalization:")
print(df)

# Verify unique values
print("\nUnique locations:")
print(df['Location'].unique())
