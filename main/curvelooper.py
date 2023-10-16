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
    r_value, r_squared, slope, intercept,  = standardcurvegenerator.generate_curve_data(chosen_dataframe)

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

#r squared stats
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

#slope and intercept value stats (this is wacky tebbaccy becuase its a numpy64 or somthing)

"""for slope in regression_dict:
    if slope in regression_dict:
        value = regression_dict[slope]
        print(f"The value for '{slope}' is '{value}'")"""

#max slope
desired_key = 'slope'
max_slope = None

for entry, nested_dict in regression_dict.items():
    if desired_key in nested_dict:
        value = nested_dict[desired_key]
        if max_slope is None or value > max_slope:
            max_slope = value

#min slope
desired_key = 'slope'
min_slope = None

for entry, nested_dict in regression_dict.items():
    if desired_key in nested_dict:
        value = nested_dict[desired_key]
        if min_slope is None or value < min_slope:
            min_slope = value

#median slope
desired_key = 'slope'

median_slope = [nested_dict[desired_key] for nested_dict in regression_dict.values() if desired_key in nested_dict]

median_slope = np.median(median_slope)

#average slope
desired_key = 'slope'

avg_slope = [nested_dict[desired_key] for nested_dict in regression_dict.values() if desired_key in nested_dict]

avg_slope = np.mean(avg_slope)

print("Slope")
print("Min slope:", min_slope)
print("Max slope:", max_slope)
print("Median slope:", median_slope)
print("Average slope:", avg_slope)
print("")

#intercept value stats 

#max intercept
desired_key = 'intercept'
max_intercept = None

for entry, nested_dict in regression_dict.items():
    if desired_key in nested_dict:
        value = nested_dict[desired_key]
        if max_intercept is None or value > max_intercept:
            max_intercept = value

#min intercept
desired_key = 'intercept'
min_intercept = None

for entry, nested_dict in regression_dict.items():
    if desired_key in nested_dict:
        value = nested_dict[desired_key]
        if min_intercept is None or value < min_intercept:
            min_intercept = value

#median intercept
desired_key = 'intercept'

median_intercept = [nested_dict[desired_key] for nested_dict in regression_dict.values() if desired_key in nested_dict]

median_intercept = np.median(median_intercept)

#average intercept
desired_key = 'intercept'

avg_intercept = [nested_dict[desired_key] for nested_dict in regression_dict.values() if desired_key in nested_dict]

avg_intercept = np.mean(avg_intercept)

print("Intercept")
print("Min intercept:", min_intercept)
print("Max intercept:", max_intercept)
print("Median intercept:", median_intercept)
print("Average intercept:", avg_intercept)
print("")

#plotting the figures

x = np.linspace(start=0, stop=10, num=100)  # This creates an array of 100 numbers spaced between 0 and 10.

# Use the min and max intercept and intercept values from your previous code.
# Correcting the variable naming
min_intercept_value = min_intercept
max_intercept_value = max_intercept

# Calculate y values for the regression lines.
y_min = min_intercept_value * x + min_intercept
y_max = max_intercept_value * x + max_intercept


# Plotting
plt.figure(figsize=(10, 6))

# Plotting the regression lines.
plt.plot(x, y_min, label="Minimum slope & intercept", color='red')
plt.plot(x, y_max, label="Maximum slope & Intercept", color='blue')

# Setting up labels, titles, and legends.
plt.title('Regression lines using the minimum and maximum slope and intercepts')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()

# Display the plot.
plt.grid(True)
plt.tight_layout()
plt.show()