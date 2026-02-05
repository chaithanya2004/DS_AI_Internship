# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:20:01 2026

@author: User
"""

dict={"name":"deepa","Rollno":4};
print(dict);
student={"name":"Deepa","Age":21,"Branch":"Enginnering"};
print(student["name"]);
student["age"]=23;
student["city"]="Delhi";
print(student)
marks = {"math": 80, "science": 75, "english": 85}

print(marks.get("math"))
print(marks.get("history", 0))

for subject, score in marks.items():
    print(subject, score)
marks.update({"maths":89});
purchases={"name":"deepa","amount":56000}

for name ,amount in purchases.items():
    print(f"{name} spent{amount}");
    print(purchases.keys);
 
n=int(input("Enter the no of user"));
userpurchases={};
for i in range(n):
    name=input("Enter your name ");
    amount=int(input(f"Enter your amount for item{name}"));
    userpurchases[name]=amount;
    print("customer purchase data ",userpurchases);
    
    
purchases = {
    "Deepa": 56000,
    "Ravi": 42000,
    "Anita": 61000
}

top_customer = max(purchases, key=purchases.get)
print("Top spending customer:", top_customer)


    

    
    
    
    
    
