# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 22:35:20 2026

@author: User
"""



friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print("Intersection")
shared_intrest=friend_a & friend_b
print(shared_intrest)
print("All intrests")
all_intrests=friend_a | friend_b
print(all_intrests)
unique_to_a = friend_a - friend_b
print("Unique intrests in a")
print(unique_to_a)