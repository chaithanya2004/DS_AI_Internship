# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:44:03 2026

@author: User
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


heights = np.random.normal(loc=170, scale=10, size=1000)


income = np.random.exponential(scale=50000, size=1000)


scores = 100 - np.random.exponential(scale=10, size=1000)

datasets = {
    "Normal (Heights)": heights,
    "Right-Skewed (Income)": income,
    "Left-Skewed (Easy Exam Scores)": scores
}

for title, data in datasets.items():
    print("\n", title)
    print("Mean:", round(np.mean(data), 2))
    print("Median:", round(np.median(data), 2))
    
    plt.figure()
    sns.histplot(data, kde=True)
    plt.title(title)
    plt.show()
