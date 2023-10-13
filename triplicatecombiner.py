#!/usr/bin/env python3

import csv
import pandas as pd
from itertools import combinations, islice, product
import dataprep

#variables
curve_num = 1000

#reads in csv of data
quant = dataprep.replicate_data


#adds unqiue replicate id
quant['unique_id'] = quant.groupby('copies').cumcount() + 1

#makes the copies str a number
quant['unique_id'] = quant['copies'].astype(str) + '_' + quant['unique_id'].astype(str)

#initialise a copies dictionary
copy_number_dict = {}

# Generate combinations of triplicates for each copy number
for copy_number in set(quant['copies']):
    copy_subset = quant[quant['copies'] == copy_number]
    triplicate_combinations = list(combinations(copy_subset['unique_id'], 3))
    copy_number_dict[copy_number] = triplicate_combinations

# Generate all possible combinations of three unique elements, each from a different copy number
final_combinations = list(islice(product(*copy_number_dict.values()), curve_num))

#initialise a dictionary for the combinations
result_dict = {}

#adds curves to the dictionary
for i, final_combo in enumerate(final_combinations):
    subset_ids = [item for sublist in final_combo for item in sublist]
    subset = quant[quant['unique_id'].isin(subset_ids)]
    result_dict[f'Combination_{i + 1}'] = subset[['Ct', 'copies', 'unique_id']].copy()
"""
#retrives unqiue standard curves
for key, df in result_dict.items():
    print(f"Standard Curve: {key}")
    print(df)
    print("\n")
"""
#retrive selected standard curve
#chosen_key = 'Combination_666'
#chosen_dataframe = result_dict[chosen_key]
#print(f"DataFrame: {chosen_key}")
#print(chosen_dataframe)

