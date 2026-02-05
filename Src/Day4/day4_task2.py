# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 22:25:11 2026

@author: User
"""
print("Original")
raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(raw_logs)
print("Unique list")
unique_users={"ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"}
print(unique_users);
print("Membership check")
result = "ID05" in unique_users
print(result);
raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"];
unique_users = set(raw_logs);
print("Length of original list:", len(raw_logs))
print("Length of set (unique users):", len(unique_users))