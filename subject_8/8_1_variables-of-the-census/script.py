# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# Task 1: View the first five rows of the dataframe
print("Task 1 - First five rows of the census dataframe:")
print(census.head())
print()

# Task 2: Assess variable types based on .head() output and the provided description
# Variable types assessment is done manually by reviewing the data

# Task 3: Check the data types of the dataframe
print("Task 3 - Data types of the dataframe:")
print(census.dtypes)
print()

# Task 4: Check unique values in birth_year
print("Task 4 - Unique values in birth_year column (before cleaning):")
print(census['birth_year'].unique())
print()

# Task 5: Replace missing values in birth_year with 1967 and recheck unique values
census['birth_year'] = census['birth_year'].replace('missing', '1967')
print("Task 5 - Unique values in birth_year column (after replacing 'missing' with '1967'):")
print(census['birth_year'].unique())
print()

# Task 6: Change birth_year datatype to int and verify
census['birth_year'] = census['birth_year'].astype(int)
print("Task 6 - Data types after converting birth_year to integer:")
print(census.dtypes)
print()

# Task 7: Calculate and print the average birth year
print("Task 7 - Average birth year calculation:")
print("Average birth year:", census['birth_year'].mean())
print()

# Task 8: Convert higher_tax to an ordered categorical datatype
tax_order = ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree']
census['higher_tax'] = pd.Categorical(census['higher_tax'], categories=tax_order, ordered=True)
print("Task 8 - Unique values in higher_tax after converting to ordered categorical:")
print(census['higher_tax'].unique())
print()

# Task 9: Label encodes higher_tax and calculates the median
census['higher_tax_encoded'] = census['higher_tax'].cat.codes
print("Task 9 - Label encoding higher_tax and calculating median sentiment:")
print("Median sentiment on higher taxes:", census['higher_tax_encoded'].median())
print()

# Task 10: One-Hot Encode marital_status
census_encoded = pd.get_dummies(census, columns=['marital_status'])
print("Task 10 - One-hot encoded dataframe (first 5 rows):")
print(census_encoded.head())
print()

# Task 11: Additional operations
print("Task 11 - Additional operations:")

# Create marital_codes by label encoding marital_status
marital_status_order = census['marital_status'].unique()
census['marital_codes'] = census['marital_status'].astype('category').cat.codes
print("Label encoding marital_status:")
print(census[['marital_status', 'marital_codes']].head())
print()

# Create age_group based on birth_year in five-year increments
census['age_group'] = pd.cut(2023 - census['birth_year'],
                             bins=range(0, 101, 5),
                             labels=[f"{i}-{i + 4}" for i in range(0, 100, 5)])
print("Creating age groups based on birth year:")
print(census[['birth_year', 'age_group']].head())
print()

# Label encodes age_group
census['age_group_encoded'] = census['age_group'].cat.codes
print("Label encoding age groups:")
print(census[['age_group', 'age_group_encoded']].head())
