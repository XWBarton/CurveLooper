#!/usr/bin/env python3

#Standard Curve Generator

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter
import dataprep, sys, pickle
from scipy import stats

#retrive the standard curve data (just one combo) from curvelooper.py
with open('data.pkl', 'rb') as file:
    curveData = pickle.load(file)

print("Data received by Standard Curve Generator:")
print(curveData)

#define the copies and CtValue data
copies = curveData['copies'].values
CtValue = curveData['Ct'].values

#adujust plot size
fig = plt.figure(figsize=(12, 6))

log_copies = np.log10(copies)

# Perform linear regression on the log-transformed x-values
slope, intercept, r_value, p_value, std_err = linregress(log_copies, CtValue)

# Predicted values using the linear regression equation
predicted_values = slope * log_copies + intercept

# Plotting the data and the linear regression line with the original x-values
plt.scatter(copies, CtValue, label='Data')
plt.plot(copies, predicted_values, color='red', label='Linear Regression')

# Adding labels and title
plt.xlabel('Copies')
plt.ylabel('Ct Value')
plt.xscale('log')  # Set x-axis to log scale

# Displaying the legend
plt.legend()

# Show the plot
#plt.show()

# Output the slope, intercept, and other regression statistics
#print("R-value:", r_value)
#print ("R^2-value:", pow(r_value, 2))
#print("Standard Curve Equation: y =", slope, "x +", intercept)




