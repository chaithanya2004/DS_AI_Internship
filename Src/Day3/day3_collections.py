# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 20:57:15 2026

@author: User
"""
print("List");
list=[1,2,3,4,5,6];
print(list)
print()
print("tuple");
tuple=(3,10);
print(tuple)
a=[100,200,300,400,500];
print("Slicing")
print(a[3:1]);
print(a[-3:-1])
print("Append");
l1=[200,300,400,500];
l1.append(800);
print(l1);
print("Remove");
a=[300,700]
l1.remove(500);
print(l1);
print("Step ");
l2=[200,300,500,600,800,700];
print(l2[1:6:2]);
print("Insert");
l1.insert(3,900);
print(l1);
print("Sort");
l3=[4,2,1,5,7];
l3.sort();
print(l3);
l3.reverse();
print(l3);
print("Extend")
data = [2, 4, 6]
data.extend([7, 8, 9])
print(data)


