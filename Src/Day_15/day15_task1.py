# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:00:59 2026

@author: User
"""

import random

trials = 1000
count_sum_7 = 0

for i in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Experimental Probability of sum = 7:", experimental_probability)
print("Theoretical Probability:", 1/6)

    
    




