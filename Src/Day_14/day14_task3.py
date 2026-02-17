# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:58:19 2026

@author: User
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


X = np.linspace(1, 10, 100).reshape(-1, 1)
y = 4*X.flatten()**2 + 3*X.flatten() + 5 + np.random.randn(100)*20


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)


poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)


print("Linear Regression R² Score:", round(r2_linear, 3))
print("Polynomial Regression R² Score:", round(r2_poly, 3))

print("\nConclusion:")
if r2_poly > r2_linear:
    print("Polynomial features improved the model performance.")
else:
    print("Polynomial features did not improve the model performance.")