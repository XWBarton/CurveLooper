#!/usr/bin/env python3

#Standard Curve Generator

import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter
import dataprep

copies = dataprep.replicate_data['copies'].values
CtValue = dataprep.replicate_data['Ct'].values

fig = plt.figure(figsize=(12, 6))

slope, intercept, r_value, p_value, std_err = linregress(np.log10(copies), CtValue)
plt.scatter(copies, CtValue, label='Data', alpha=0.5)

x_values = np.linspace(min(copies), max(copies), 100)
plt.plot(x_values, slope * np.log10(x_values) + intercept, color='red', label='Linear Fit')
plt.xscale('log')

formatter = ScalarFormatter()
formatter.set_scientific(False)
plt.gca().xaxis.set_major_formatter(formatter)

plt.xlabel('gBlock Copies')
plt.ylabel('Ct Value')
plt.title('Standard Curve')
plt.legend()
plt.show()

#Figures
print(f"R-value: {r_value}")
print(f"R-squared: {r_value**2}")
print(f"Line equation: y = {slope:.4f} * log10(x) + {intercept:.4f}")