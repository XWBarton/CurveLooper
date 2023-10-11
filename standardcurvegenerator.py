#Standard Curve Generator

import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter

replicate_data = pd.read_csv('/Users/xavierbarton/Library/CloudStorage/OneDrive-Personal/Documents/Murdoch/PhD/Programming/CurveLooper/Standard Curves/Bacterial Standard Curve.csv')

#convert copies from str to num
replicate_data['copies'] = replicate_data['copies'].str.replace(',', '').astype(float)

#Remove NTC and lower thresholds
replicate_data = replicate_data[replicate_data['copies'] != 0] #NTC
replicate_data = replicate_data[replicate_data['copies'] != 0.01]
replicate_data = replicate_data[replicate_data['copies'] != 0.1]
replicate_data = replicate_data[replicate_data['copies'] != 1]
replicate_data = replicate_data[replicate_data['copies'] != 10]
replicate_data = replicate_data[replicate_data['copies'] != 100]
print(replicate_data)

copies = replicate_data['copies'].values
CtValue = replicate_data['Ct'].values

"""
#String number test

test = max(copies)

if isinstance(test, str):
    print("It's a string.")
else:
    print("It's not a string.")

# Test if it's a number
if isinstance(test, (int, float)):
    print("It's a number.")
else:
    print("It's not a number.")
"""

#print(x_values)
#print(y_values)
fig = plt.figure(figsize=(12, 6))

slope, intercept, r_value, p_value, std_err = linregress(np.log10(copies), CtValue)
plt.scatter(copies, CtValue, label='Data', alpha=0.5)

x_values = np.linspace(min(copies), max(copies), 100)
plt.plot(x_values, slope * np.log10(x_values) + intercept, color='red', label='Linear Fit')
plt.xscale('log')

custom_ticks = [1000, 10000, 100000, 1000000, 10000000]
plt.xticks(custom_ticks, [f'{tick:.2e}' for tick in custom_ticks])

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