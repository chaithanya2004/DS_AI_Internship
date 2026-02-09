# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 10:30:42 2026

@author: User
"""
#file handling
file = open("sample.txt", "w")
file.write("Hello, this is a file handling example")
file.close()

# reading file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#context manager
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
    
    
#try  and excpet
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the filename.")
    
    
#csv file
import csv; 
with open("Student.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
import pandas as pd;
df = pd.read_csv("student.csv")
print(df)

import pandas as pd;
df=pd.read_excel("data.xlsx");
print(df) ;      
