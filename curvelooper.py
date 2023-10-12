#!/usr/bin/env python3

import triplicatecombiner
import subprocess

#print(triplicatecombiner.result_dict)

#retrive selected standard curve
chosen_key = 'Combination_99'
chosen_dataframe = triplicatecombiner.result_dict[chosen_key]
print(f"DataFrame: {chosen_key}")
print(chosen_dataframe)

def main():
    data_to_pass = chosen_dataframe

    # Save DataFrame to CSV
    data_to_pass.to_csv('data_to_pass.csv', index=False)

    # Run myscript.py
    subprocess.run(['python3', 'standardcurvegenerator.py', 'data_to_pass.csv'])

if __name__ == "__main__":
    main()


