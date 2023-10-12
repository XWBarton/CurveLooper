#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter

#prepare data

replicate_data = pd.read_csv('Standard Curves/Ixodida Standard Curve .csv')

"""
#USER INPUT
file_name = input("Enter the name of the CSV file: ")

try:
    # Read the CSV file using pandas
    replicate_data = pd.read_csv(file_name)

    # Display the data (you can modify this part based on your needs)
    print(replicate_data)

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except pd.errors.EmptyDataError:
    print(f"The file '{file_name}' is empty.")

except pd.errors.ParserError:
    print(f"Error parsing CSV file '{file_name}'. Check if it's a valid CSV file.")

except Exception as e:
    print(f"An error occurred: {e}")
"""

#convert copies from str to num
replicate_data['copies'] = replicate_data['copies'].str.replace(',', '').astype(float)


#Remove NTC and lower thresholds
replicate_data = replicate_data[replicate_data['copies'] != 0] #NTC
replicate_data = replicate_data[replicate_data['copies'] != 0.01]
replicate_data = replicate_data[replicate_data['copies'] != 0.1]
replicate_data = replicate_data[replicate_data['copies'] != 1]
replicate_data = replicate_data[replicate_data['copies'] != 10]
replicate_data = replicate_data[replicate_data['copies'] != 100]

#print(replicate_data)

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