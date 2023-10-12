#!/usr/bin/env python3

#Standard Curve Generator

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter
import dataprep
import sys

def my_function(data_received):
    print("Data received in my_function:", data_received)

if __name__ == "__main__":
    # The first command-line argument is the script name, so we start from index 1
    data_from_main_script = sys.argv[1]
    my_function(data_from_main_script)

#copies = dataprep.replicate_data['copies'].values
#CtValue = dataprep.replicate_data['Ct'].values

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
plt.show()

# Output the slope, intercept, and other regression statistics
print("R-value:", r_value)
print ("R^2-value:", pow(r_value, 2))
print("Standard Curve Equation: y =", slope, "* x +", intercept)
