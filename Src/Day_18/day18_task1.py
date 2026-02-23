# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 19:28:40 2026

@author: User
"""

import sqlite3
import pandas as pd


conn = sqlite3.connect("internship.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT NOT NULL,
    track TEXT NOT NULL
)
""")



cursor.execute("DELETE FROM mentors")  

mentor_data = [
    (101, "Dr. Sharma", "Data Science"),
    (102, "Mr. Verma", "Web Dev"),
    (103, "Ms. Iyer", "Cyber Security")
]

cursor.executemany("""
INSERT INTO mentors (mentor_id, mentor_name, track)
VALUES (?, ?, ?)
""", mentor_data)

conn.commit()


join_query = """
SELECT 
    i.name AS Intern_Name,
    i.track AS Track,
    m.mentor_name AS Mentor_Name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track
"""



df = pd.read_sql_query(join_query, conn)

print("Interns with their Mentors:\n")
print(df)

conn.close()