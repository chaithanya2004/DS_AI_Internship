# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 11:50:40 2026

@author: User
"""

billamount=float(input("Enter bill amount"));
people=int(input("Enter the number of people"));
Share=billamount/people;
print(f"Total Bill: {billamount}. Each person pays: {Share}")
print(type(billamount));
print(type(Share));