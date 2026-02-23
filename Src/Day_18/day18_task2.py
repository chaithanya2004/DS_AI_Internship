# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 21:22:23 2026

@author: User
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")


filter_query = """
SELECT id, name, track, stipend
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
"""

df_filter = pd.read_sql_query(filter_query, conn)

print("Data Science Interns with Stipend > 5000:\n")
print(df_filter)




aggregate_query = """
SELECT track, AVG(stipend) AS Average_Stipend
FROM interns
GROUP BY track
"""

df_avg = pd.read_sql_query(aggregate_query, conn)

print("\nAverage Stipend Per Track:\n")
print(df_avg)




count_query = """
SELECT track, COUNT(*) AS Intern_Count
FROM interns
GROUP BY track
"""

df_count = pd.read_sql_query(count_query, conn)

print("\nNumber of Interns Per Track:\n")
print(df_count)


# Close connection
conn.close()