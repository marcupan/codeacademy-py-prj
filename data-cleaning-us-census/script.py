import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

# Task 1: List all CSV files in directory to inspect naming
csv_files = glob.glob("*.csv")
print("CSV files available:", csv_files)

# Task 2: Read and concatenate all state CSVs into one DataFrame
census_dfs = []
for file in csv_files:
    # include all state CSV files
    df_part = pd.read_csv(file)
    census_dfs.append(df_part)
us_census = pd.concat(census_dfs, ignore_index=True)

# Task 3: Examine columns and dtypes
print(us_census.columns)
print(us_census.dtypes)

# Task 4: Preview first rows
print(us_census.head())

# Task 5: Clean 'Income' column (remove '$' and ',') and convert to float
us_census['Income'] = (
    us_census['Income']
    .str.replace(r"[\$,]", "", regex=True)
    .astype(float)
)

# Task 6: Split 'GenderPop' into 'Men' and 'Women'
gender_split = us_census['GenderPop'].str.split("_", expand=True)
us_census['Men'] = gender_split[0]
us_census['Women'] = gender_split[1]

# Task 7: Remove letter suffixes and convert to numeric (handle missing)
us_census['Men'] = us_census['Men'].str.replace('M', '', regex=False)
us_census['Men'] = pd.to_numeric(us_census['Men'], errors='coerce')

us_census['Women'] = us_census['Women'].str.replace('F', '', regex=False)
us_census['Women'] = us_census['Women'].replace('', np.nan)
us_census['Women'] = pd.to_numeric(us_census['Women'], errors='coerce')

# Task 8: Scatterplot of Income vs Women count
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Women (count)')
plt.ylabel('Income (USD)')
plt.title('Income vs. Women Population')
plt.show()
plt.clf()

# Task 9: Fill NaNs in 'Women' using TotalPop - Men
print("NaNs in Women before fill:", us_census['Women'].isna().sum())
us_census['Women'] = us_census['Women'].fillna(
    us_census['TotalPop'] - us_census['Men']
)
print("NaNs in Women after fill:", us_census['Women'].isna().sum())

# Task 10: Check for duplicate rows
print("Duplicates found:", us_census.duplicated().sum())

# Task 11: Drop duplicate rows
us_census = us_census.drop_duplicates()
print("Duplicates after drop:", us_census.duplicated().sum())

# Task 12: Re-plot scatter after cleaning
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Women (count)')
plt.ylabel('Income (USD)')
plt.title('Income vs. Women Population (Cleaned)')
plt.show()
plt.clf()

# Task 13: Identify race percentage columns
race_cols = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']
print("Race columns:", race_cols)

# Task 14: Clean and plot histograms for each race column
for col in race_cols:
    us_census[col] = us_census[col].str.rstrip('%').astype(float)
    plt.hist(us_census[col].dropna(), bins=20, edgecolor='black')
    plt.xlabel(f"{col} (%)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {col}")
    plt.show()
    plt.clf()

# Task 15: Additional analyses can be added below
# e.g., plot Income vs percent White, explore correlations, etc.
