# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# Task 1: View the first five rows of the dataframe
print(census.head())

# Task 2: Assess variable types based on .head() output and the provided description
# Variable types assessment is done manually by reviewing the data

# Task 3: Check the data types of the dataframe
print(census.dtypes)

# Task 4: Check unique values in birth_year
print(census['birth_year'].unique())

# Task 5: Replace missing values in birth_year with 1967 and recheck unique values
census['birth_year'] = census['birth_year'].replace('missing', '1967')
print(census['birth_year'].unique())

# Task 6: Change birth_year datatype to int and verify
census['birth_year'] = census['birth_year'].astype(int)
print(census.dtypes)

# Task 7: Calculate and print the average birth year
print("Average birth year:", census['birth_year'].mean())

# Task 8: Convert higher_tax to an ordered categorical datatype
tax_order = ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree']
census['higher_tax'] = pd.Categorical(census['higher_tax'], categories=tax_order, ordered=True)
print(census['higher_tax'].unique())

# Task 9: Label encode higher_tax and calculate the median
census['higher_tax_encoded'] = census['higher_tax'].cat.codes
print("Median sentiment on higher taxes:", census['higher_tax_encoded'].median())

# Task 10: One-Hot Encode marital_status
census_encoded = pd.get_dummies(census, columns=['marital_status'])
print(census_encoded.head())

# Task 11: Additional operations
# Create marital_codes by label encoding marital_status
marital_status_order = census['marital_status'].unique()
census['marital_codes'] = census['marital_status'].astype('category').cat.codes
print(census[['marital_status', 'marital_codes']].head())

# Create age_group based on birth_year in five-year increments
census['age_group'] = pd.cut(2023 - census['birth_year'],
                             bins=range(0, 101, 5),
                             labels=[f"{i}-{i + 4}" for i in range(0, 100, 5)])
print(census[['birth_year', 'age_group']].head())

# Label encode age_group
census['age_group_encoded'] = census['age_group'].cat.codes
print(census[['age_group', 'age_group_encoded']].head())
