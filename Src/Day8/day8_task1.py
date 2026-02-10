# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:53:40 2026

@author: User
"""

import numpy as np;
score=np.random.randint(50,300,size=(5,3));
print("Original score")
print(score);
centerd_score=score-np.mean(score, axis=0)
print("Centerd score");
print(centerd_score)
