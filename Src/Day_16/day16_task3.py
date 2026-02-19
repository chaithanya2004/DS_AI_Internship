# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:49:30 2026

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


original_data = np.random.exponential(scale=50000, size=10000)


sample_means = []

for i in range(1000):
    sample = np.random.choice(original_data, size=30)
    sample_means.append(np.mean(sample))


plt.figure()
sns.histplot(original_data, kde=True)
plt.title("Original Skewed Distribution")
plt.show()

plt.figure()
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (CLT)")
plt.show()
