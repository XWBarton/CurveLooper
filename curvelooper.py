#!/usr/bin/env python3

import triplicatecombiner

#print(triplicatecombiner.result_dict)

#retrive selected standard curve
chosen_key = 'Combination_99'
chosen_dataframe = triplicatecombiner.result_dict[chosen_key]
print(f"DataFrame: {chosen_key}")
print(chosen_dataframe)


