# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:26:19 2026

@author: chaithanya
"""

import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
values = [300, 450, 200]
plt.subplot(1, 2, 1)
plt.bar(categories, values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.subplot(1, 2, 2)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [150, 200, 250, 300, 280]
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()