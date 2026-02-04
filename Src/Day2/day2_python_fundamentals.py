# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
age=20;
name="deepa";
print(age);
print(name);
type(age);
type(name);
print("calculator");
a=int(input("enter 1 number:"));
b=int(input("enter number 2:"));
print("1.Addition");
print("2.Substraction")
print("3.Multiplication");
print("3.division");
ch=input("enter a choice");
if ch=='1' :
   print("Result",a+b);
elif ch=='2':
    print("Result",a-b);
elif ch=='3':
    print("Result",a*b);
elif ch=='4':
    print("Result",a/b);
    
name=input("enter a string");
print("using concat")
print("Welcome"+name+"!");

name="Deepa";
print("using fstring")
print(f"Welcome {name}");
    

    
    
    
    
    
    

