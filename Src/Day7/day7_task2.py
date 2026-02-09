# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:40:19 2026

@author: User
"""

import csv

with open("Students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for name, grade, status in reader:
        if status == "Pass":
            print(name)