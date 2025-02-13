import numpy as np
import pandas as pd
from os import listdir
import os

csv_files = [f for f in listdir() if f.endswith('.csv')]
print(csv_files)
names = ['m','r','T','rho','P','l','X_H','X_He4','X_He3','X_C12','X_N14','X_O16','X_7Be','nu pp','nu B8','nu N13','nu O15','nu F17','nu Be7','nu pep','nu hep','log10(n_eN_A)']

combined_df = pd.DataFrame()


for file in csv_files:
	if file == 'rough_model.csv':
		continue
    # Read the current CSV file
	df = pd.read_csv(file)
    # Merge with the combined DataFrame
	if combined_df.empty:
		combined_df = df
	else:
		combined_df = pd.merge(combined_df, df, on="r", how="outer")

# Output the combined DataFrame to a new CSV file
output_file = "combined_output.csv"
combined_df.to_csv(output_file, index=False)

print(f"Combined DataFrame saved to {output_file}")
