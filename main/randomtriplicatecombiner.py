#!/usr/bin/env python3

import pandas as pd
from itertools import combinations as itertools_combinations
import dataprep
import time
import random
from math import comb

start_time = time.time()

#curve_num = 100000

curve_num = input("Enter the number of standard curve combinations you would like to generate: ")
try:
    curve_num = int(curve_num)
except ValueError:
    print("That's not a valid integer!")

quant = dataprep.replicate_data

# Count how many unique 'copies' categories
unique_values_count = quant['copies'].nunique()
print(f"\nNumber of gBlock dilutions: {unique_values_count}")

# Calculate combinations within each 'copies' category
unique_categories = quant['copies'].unique()

combinations = [comb(len(quant[quant['copies'] == category]), 3) for category in unique_categories]
print(f"\nCombinations for each category: {combinations}")

# Add unique replicate ID to the dataframe
quant['unique_id'] = quant.groupby('copies').cumcount() + 1
quant['unique_id'] = quant['copies'].astype(str) + '_' + quant['unique_id'].astype(str)

# Generate combinations of triplicates for each copy number and shuffle them
copy_number_dict = {copy_number: sorted(itertools_combinations(quant[quant['copies'] == copy_number]['unique_id'], 3), key=lambda x: random.random())
                    for copy_number in unique_categories}

all_triplicate_combinations = set()

# Generate random combinations using low processing power
while len(all_triplicate_combinations) < curve_num:
    random_combination = tuple(random.choice(copy_number_dict[copy_number]) for copy_number in unique_categories)
    all_triplicate_combinations.add(random_combination)

print(f"\nTotal unique combinations generated: {len(all_triplicate_combinations)}")

# Organize combinations into a dictionary
result_dict = {}
for i, combination in enumerate(all_triplicate_combinations):
    subset_ids = [item for triplet in combination for item in triplet]
    subset = quant[quant['unique_id'].isin(subset_ids)]
    result_dict[f'Combination_{i + 1}'] = subset[['Ct', 'copies', 'unique_id']].copy()

# Function to retrieve a standard curve
def retreive_selected_standard_curve(chosen_key):
    chosen_dataframe = result_dict[chosen_key]
    return chosen_dataframe

# Print the first 10 combinations after the dictionary is generated.
print("First 10 Combinations:")
for key in list(result_dict.keys())[:10]:
    print(f"\n{key}:")
    print(result_dict[key])

end_time = time.time()
print(f"\nCombiner took {end_time - start_time} seconds to run.")
