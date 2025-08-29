import pandas as pd
import numpy as np

# Load the dataset
diabetes_data = pd.read_csv('diabetes.csv')

# Initial Inspection
# Task 2: Print the first few rows of the dataset
print("Task 2 - First few rows of the dataset:")
print(diabetes_data.head())
print()

# Task 3: Count the number of columns
print("Task 3 - Dataset dimensions:")
print(f"Number of columns: {diabetes_data.shape[1]}")
print()

# Task 4: Count the number of rows
print("Task 4 - Dataset size:")
print(f"Number of rows: {diabetes_data.shape[0]}")
print()

# Further Inspection
# Task 5: Check for missing values
print("Task 5 - Missing values before replacement:")
print(diabetes_data.isnull().sum())
print()

# Task 6: Calculate summary statistics
print("Task 6 - Summary statistics (before cleaning):")
print(diabetes_data.describe())
print()

# Task 7: Note anomalies in Glucose, BloodPressure, SkinThickness, Insulin, BMI
# (e.g., min values being 0, which isn't valid in some cases)
print("Task 7 - Identifying anomalies:")
print("Note: 0 values in medical measurements like Glucose, BloodPressure are impossible")
print()

# Replace 0 with NaN in specific columns
columns_to_replace = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
diabetes_data[columns_to_replace] = diabetes_data[columns_to_replace].replace(0, np.nan)
print("Task 8-9 - Replacing 0 values with NaN in medical columns:")
print("Columns affected:", columns_to_replace)
print()

# Task 10: Check for missing values again
print("Task 10 - Missing values after replacing 0 with NaN:")
print(diabetes_data.isnull().sum())
print()

# Task 11: Print rows with missing values
missing_rows = diabetes_data[diabetes_data.isnull().any(axis=1)]
print("Task 11 - Rows with missing values (first 10):")
print(missing_rows.head(10))
print(f"Total rows with missing data: {len(missing_rows)}")
print()

# Task 12: Analyze patterns or overlaps in missing data
print("Task 12 - Analysis of missing data patterns:")
print("Review the rows above to identify patterns in missing data")
print()

# Task 13: Check data types of each column
print("Task 13 - Data types of each column:")
print(diabetes_data.dtypes)
print()

# Task 14: Check unique values in the Outcome column
print("Task 14 - Unique values in Outcome column (before cleaning):")
print(diabetes_data['Outcome'].unique())
print()

# Task 15: Resolve issue with Outcome data type
# Replace 'O' with 0 in the Outcome column
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace({'O': '0'})

# Convert Outcome to integers
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(int)

# Verify the conversion
print("Task 15 - Fixing Outcome column:")
print("Unique values in Outcome column after cleaning:")
print(diabetes_data['Outcome'].unique())
print("Data types after fixing Outcome column:")
print(diabetes_data.dtypes)
print()

# Extend Exploration
# Task 16: Value counts for each column
print("Task 16 - Value counts for each column:")
for column in diabetes_data.columns:
    print(f"\n{column}:")
    print(diabetes_data[column].value_counts().head())

print()

# Replace NaN values with median for each column
print("Task 17 - Filling missing values with median:")
diabetes_data.fillna(diabetes_data.median(), inplace=True)

# Verify no missing values remain
print("Missing values after filling with median:")
print(diabetes_data.isnull().sum())
print()

# Final summary statistics after cleaning
print("Task 18 - Final summary statistics after cleaning:")
print(diabetes_data.describe())