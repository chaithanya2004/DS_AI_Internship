# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:49:16 2026

@author: User
"""

def calc_rectangle(length, width):
    area=length*width;
    perimeter=2*(length+width);
    return(area,perimeter)
length=int(input("Enter the length of rectangle"));
width=int(input("Enter the width of the rectangle"));
area,perimeter=calc_rectangle(length,width);
print("Area:",area,",","Perimeter:",perimeter);

   