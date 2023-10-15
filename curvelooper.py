#!/usr/bin/env python3

import randomtriplicatecombiner
import subprocess, statistics
import pandas as pd
import standardcurvegenerator
import matplotlib.pyplot as plt
import numpy as np
from statistics import median

chosen_key = "Combination"

#initalise the dictionary for the regression statistics
regression_dict = {}  # Initialize an empty dictionary to store results

for i in range(1, randomtriplicatecombiner.curve_num + 1):
    current_key = f'{chosen_key}_{i}'
    
    # Retrieve the chosen_dataframe for the current key
    chosen_dataframe = randomtriplicatecombiner.retreive_selected_standard_curve(current_key)

    # exec(open("standardcurvegenerator.py").read())
    r_value, r_squared, slope, intercept = standardcurvegenerator.generate_curve_data(chosen_dataframe)

     # Store results in the dictionary
    regression_dict[current_key] = {
        'r_value': r_value,
        'r_squared':  r_squared,
        'slope': slope,
        'intercept': intercept
    }

print("")
print(f"For {randomtriplicatecombiner.curve_num} combinations:")

#r value stats
all_r_values = [entry['r_value'] for entry in regression_dict.values()]

min_r = min(all_r_values)
max_r = max(all_r_values)
median_r = statistics.median(all_r_values)
average_r = statistics.mean(all_r_values)

#print r value stats
print("")
print("R value")
print("Min r_value:", min_r)
print("Max r_value:", max_r)
print("Median r_value:", median_r)
print("Average r_value:", average_r)
print("")

#r value stats
all_r_sqaured = [entry['r_squared'] for entry in regression_dict.values()]
min_r_sqaured = min(all_r_sqaured)
max_r_sqaured = max(all_r_sqaured)
median_r_squared = statistics.median(all_r_sqaured)
average_r_squared = statistics.mean(all_r_sqaured)

#print r squared stats
print("R squared")
print("Min r_squared:", min_r_sqaured)
print("Max r_squared:", max_r_sqaured)
print("Median r_squared:", median_r_squared)
print("Average r_squared:", average_r_squared)
print("")

#slope value stats
all_slope = [entry['slope'] for entry in regression_dict.values()]

slopes = [(all_slope[i+1] - all_slope[i]) for i in range(len(all_slope)-1)]
min_slope = min(slopes)
max_slope = max(slopes)
average_slope = sum(slopes) / len(slopes)
median_slope = median(slopes)

print("Slope")
print("Minimum slope:", min_slope)
print("Max slope:", max_slope)
print("Average slope:", average_slope)
print("Median slope:", median_slope)
print("")

#intercept stats
all_intercept = [entry['intercept'] for entry in regression_dict.values()]

intercepts = [(all_intercept[i+1] - all_intercept[i]) for i in range(len(all_intercept)-1)]

min_intercept = min(intercepts)
max_intercept = max(intercepts)
average_intercept = sum(intercepts) / len(intercepts)
median_intercept = median(intercepts)

print("Intercept")
print("Minimum intercept:", min_intercept)
print("Max intercept:", max_intercept)
print("Average intercept:", average_intercept)
print("Median intercept:", median_intercept)
print("")


#plotting the figures

x = np.linspace(start=0, stop=10, num=100)  # This creates an array of 100 numbers spaced between 0 and 10.

# Use the min and max slope and intercept values from your previous code.
# Correcting the variable naming
min_slope_value = min_slope
max_slope_value = max_slope

# Calculate y values for the regression lines.
y_min = min_slope_value * x + min_intercept
y_max = max_slope_value * x + max_intercept

# Plotting
plt.figure(figsize=(10, 6))

# Plotting the regression lines.
plt.plot(x, y_min, label="Line with Min Slope & Intercept", color='red')
plt.plot(x, y_max, label="Line with Max Slope & Intercept", color='blue')

# Setting up labels, titles, and legends.
plt.title('Regression Lines for Min & Max Slope and Intercept')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()

# Display the plot.
plt.grid(True)
plt.tight_layout()
plt.show()