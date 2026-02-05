# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 21:53:36 2026

@author: User
"""

contacts={"Ramya":"9878646436","Deepa":"6758579499","Radha":"9087867584"}
print("Added new entry")
contacts["Ananya"]="9897869868";
print(contacts)
print("updated the existing contact")
contacts.update({"Deepa":"9678646436"});
print(contacts)
print("Existing contact check")
print(contacts.get("Ramya"));
print("Not existing contact check")
print(contacts.get("Roopa","contacts not found"));  
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}");