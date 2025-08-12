import pandas as pd
import numpy as np

# Load the dataset
diabetes_data = pd.read_csv('diabetes.csv')

# Initial Inspection
# Task 2: Print the first few rows of the dataset
print("First few rows of the dataset:")
print(diabetes_data.head())

# Task 3: Count the number of columns
print(f"Number of columns: {diabetes_data.shape[1]}")

# Task 4: Count the number of rows
print(f"Number of rows: {diabetes_data.shape[0]}")

# Further Inspection
# Task 5: Check for missing values
print("Missing values in each column before replacement:")
print(diabetes_data.isnull().sum())

# Task 6: Calculate summary statistics
print("Summary statistics:")
print(diabetes_data.describe())

# Task 7: Note anomalies in Glucose, BloodPressure, SkinThickness, Insulin, BMI
# (e.g., min values being 0, which isn't valid in some cases)

# Replace 0 with NaN in specific columns
columns_to_replace = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
diabetes_data[columns_to_replace] = diabetes_data[columns_to_replace].replace(0, np.nan)

# Task 10: Check for missing values again
print("Missing values in each column after replacement:")
print(diabetes_data.isnull().sum())

# Task 11: Print rows with missing values
missing_rows = diabetes_data[diabetes_data.isnull().any(axis=1)]
print("Rows with missing values:")
print(missing_rows)

# Task 12: Analyze patterns or overlaps in missing data
# Review printed rows manually for patterns

# Task 13: Check data types of each column
print("Data types of each column:")
print(diabetes_data.dtypes)

# Task 14: Check unique values in the Outcome column
print("Unique values in Outcome column before cleaning:")
print(diabetes_data['Outcome'].unique())

# Task 15: Resolve issue with Outcome data type
# Replace 'O' with 0 in the Outcome column
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace({'O': '0'})

# Convert Outcome to integers
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(int)

# Verify the conversion
print("Unique values in Outcome column after cleaning:")
print(diabetes_data['Outcome'].unique())
print("Data types of each column after fixing Outcome column:")
print(diabetes_data.dtypes)

# Extend Exploration
# Task 16: Value counts for each column
print("Value counts for each column:")
for column in diabetes_data.columns:
    print(f"{column}:")
    print(diabetes_data[column].value_counts())

# Replace NaN values with median for each column
diabetes_data.fillna(diabetes_data.median(), inplace=True)

# Verify no missing values remain
print("Missing values after filling with median:")
print(diabetes_data.isnull().sum())

# Final summary statistics after cleaning
print("Summary statistics after cleaning:")
print(diabetes_data.describe())
