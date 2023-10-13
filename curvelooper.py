#!/usr/bin/env python3

import triplicatecombiner
import subprocess
import pandas as pd
import pickle
import standardcurvegenerator
"""
#retrive selected standard curve
chosen_key = 'Combination_1'
chosen_dataframe = triplicatecombiner.result_dict[chosen_key]
print("")
print(f"Sucsessfully retrived {chosen_key} from the combiner.")
print("")

#send combination to the standard curve generator
with open('data.pkl', 'wb') as file:
    pickle.dump(chosen_dataframe, file)

exec(open("standardcurvegenerator.py").read())

#retrive regression data for this standard curve from Standard Curve Generator
print("")
print("Regression Values:")
print("R-value:", standardcurvegenerator.r_value)
print ("R^2-value:", pow(standardcurvegenerator.r_value, 2))
print("Standard Curve Equation: y =", standardcurvegenerator.slope, "x +", standardcurvegenerator.intercept)
print("")
"""
chosen_key = 'Combination'

for i in range(1, 1001):
    current_key = f'{chosen_key}_{i}'
    
    # Retrieve the chosen_dataframe for the current key
    chosen_dataframe = triplicatecombiner.result_dict[current_key]
    
    print("")
    print(f"Successfully retrieved {current_key} from the combiner.")
    print("")

    # Send the combination to the standard curve generator
    with open('data.pkl', 'wb') as file:
        pickle.dump(chosen_dataframe, file)

    exec(open("standardcurvegenerator.py").read())

    # Retrieve regression data for this standard curve from Standard Curve Generator
    print("")
    print("Regression Values:")
    print("R-value:", standardcurvegenerator.r_value)
    print("R^2-value:", pow(standardcurvegenerator.r_value, 2))
    print("Standard Curve Equation: y =", standardcurvegenerator.slope, "x +", standardcurvegenerator.intercept)
    print("")
