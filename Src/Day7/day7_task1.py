# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:21:59 2026

@author: User
"""

name=input("Enter your name");
daily_log=input("Enter your daily_log");
with open("journal.txt","a") as file:
    file.write("Name:"+name +"Daily_log:"+ " - " + daily_log+ "\n")