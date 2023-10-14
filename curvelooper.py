#!/usr/bin/env python3

import triplicatecombiner
import subprocess, statistics
import pandas as pd
import standardcurvegenerator
import matplotlib.pyplot as plt
import numpy as np

chosen_key = "Combination"

#initalise the dictionary for the regression statistics
regression_dict = {}  # Initialize an empty dictionary to store results

for i in range(1, 101):
    current_key = f'{chosen_key}_{i}'
    
    # Retrieve the chosen_dataframe for the current key
    chosen_dataframe = triplicatecombiner.retreive_selected_standard_curve(current_key)

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
print(f"For {triplicatecombiner.curve_num} combinations:")

#r value stats
all_r_values = [entry['r_value'] for entry in regression_dict.values()]

min_r = min(all_r_values)
max_r = max(all_r_values)
median_r = statistics.median(all_r_values)
average_r = statistics.mean(all_r_values)

# Print or use the results as needed
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

# Print or use the results as needed
print("R squared")
print("Min r_squared:", min_r_sqaured)
print("Max r_squared:", max_r_sqaured)
print("Median r_squared:", median_r_squared)
print("Average r_squared:", average_r_squared)
print("")

"""#equation
# Extract slope and intercept values
slopes = [entry['slope'] for entry in regression_dict.values()]
intercepts = [entry['intercept'] for entry in regression_dict.values()]

# Find minimum and maximum slope and intercept
min_slope = min(slopes)
max_slope = max(slopes)
min_intercept = min(intercepts)
max_intercept = max(intercepts)

# Generate x values for the plot
x_values = np.linspace(min(log_copies), max(log_copies), 100)

# Plot the minimum and maximum regression lines
plt.scatter(log_copies, CtValue, label='Data Points')  # Your actual data points
plt.plot(x_values, min_slope * x_values + min_intercept, label='Min Regression Line', linestyle='--')
plt.plot(x_values, max_slope * x_values + max_intercept, label='Max Regression Line', linestyle='--')

# Customize the plot
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Min and Max Regression Lines')
plt.legend()
plt.show()"""