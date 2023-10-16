#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter
import csv

#prepare data

#replicate_data = pd.read_csv('Standard Curves/Ixodida Standard Curve .csv')

#USER INPUT
file_name = input("Enter the path of the CSV file: ")

try:
    # Read the CSV file using pandas
    replicate_data = pd.read_csv(file_name)

    # Display the data (you can modify this part based on your needs)
    #print(replicate_data)

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except pd.errors.EmptyDataError:
    print(f"The file '{file_name}' is empty.")

except pd.errors.ParserError:
    print(f"Error parsing CSV file '{file_name}'. Check if it's a valid CSV file.")

except Exception as e:
    print(f"An error occurred: {e}")

#convert copies from str to num
replicate_data['copies'] = replicate_data['copies'].str.replace(',', '').astype(float)

"""
#Remove NTC and lower thresholds
replicate_data = replicate_data[replicate_data['copies'] != 0] #NTC
replicate_data = replicate_data[replicate_data['copies'] != 0.01]
replicate_data = replicate_data[replicate_data['copies'] != 0.1]
replicate_data = replicate_data[replicate_data['copies'] != 1]
replicate_data = replicate_data[replicate_data['copies'] != 10]
replicate_data = replicate_data[replicate_data['copies'] != 100]
"""

#User excluded values
excluded_values = input("Enter the gBlock copy numbers you want to exclude separated by commas (e.g., 0, 0.01, 0.1), or leave blank to skip: ")

if excluded_values.strip():
    # Convert to list of floats
    excluded_values = [float(value.strip()) for value in excluded_values.split(",")]

    # Filter data
    for value in excluded_values:
        replicate_data = replicate_data[replicate_data['copies'] != value]

print(replicate_data)