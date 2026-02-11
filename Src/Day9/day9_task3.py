# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:00:09 2026

@author: User
"""
import pandas as pd;
usernames=pd.Series(['Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print("Original series");
print(usernames);
print('Removing whitespace');
print(usernames.str.strip())
print("Converting to Lowercase ")
print(usernames.str.lower())
print("word which contains letter  'a'" )
print(usernames.str.contains('a'));
