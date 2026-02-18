# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:43:11 2026

@author: User
"""

import random

trials = 100000

ind_count = 0

for _ in range(trials):
    if random.choice(["H", "T"]) == "H" and random.randint(1, 6) == 6:
        ind_count += 1

print("Independent Probability:", ind_count / trials)
print("Theoretical:", 1/12)


dep_count = 0

for _ in range(trials):
    bag = ["R"]*5 + ["B"]*5
    first = random.choice(bag)
    bag.remove(first)
    
    if first == "R" and random.choice(bag) == "R":
        dep_count += 1

print("\nDependent Probability:", dep_count / trials)
print("Theoretical:", 2/9)
