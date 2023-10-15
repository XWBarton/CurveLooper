#!/usr/bin/env python3

import pandas as pd
from itertools import combinations as itertools_combinations, islice, product
import dataprep
import time
import csv
from math import comb

start_time = time.time()

curve_num = 100000
quant = dataprep.replicate_data


#how many unique copies categories
unique_values_count = quant['copies'].nunique()
print("")
print(f"Number of gBlock dilutions: {unique_values_count}")

#find number of possible combos

unique_categories = quant['copies'].unique()

combinations = [comb(len(quant[quant['copies'] == category]), 3) for category in unique_categories]

# Multiply the combinations together
total_combinations = 1
for combination in combinations:
    total_combinations *= combination
print("")
print(f"Total number of combinations possible: {total_combinations}")

#adds unqiue replicate id
quant['unique_id'] = quant.groupby('copies').cumcount() + 1

#makes the copies str a number
quant['unique_id'] = quant['copies'].astype(str) + '_' + quant['unique_id'].astype(str)

#initialise a copies dictionary
copy_number_dict = {}

# Generate combinations of triplicates for each copy number
for copy_number in set(quant['copies']):
    copy_subset = quant[quant['copies'] == copy_number]
    triplicate_combinations = list(itertools_combinations(copy_subset['unique_id'], 3))
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

# retrive selected standard curve
def retreive_selected_standard_curve(chosen_key):
    chosen_dataframe = result_dict[chosen_key]
    #print(f"DataFrame: {chosen_key}")
    #print(chosen_dataframe)
    return chosen_dataframe

end_time = time.time()
elapsed_time = end_time - start_time
print("")
print(f"Single threaded script took {elapsed_time} seconds to run.")