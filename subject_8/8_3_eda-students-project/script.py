# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Task 1: Print the first few rows of data
print("Task 1 - First few rows of student data:")
print(students.head())
print()

# Task 2: Print summary statistics for all columns
print("Task 2 - Summary statistics for all columns:")
print(students.describe())
print()

# Determine if more students live in urban or rural areas
urban_count = students['address'].value_counts().get('U', 0)
rural_count = students['address'].value_counts().get('R', 0)
print("Task 3 - Urban vs Rural distribution:")
print(f"Urban: {urban_count}, Rural: {rural_count}")
print()

# Task 3: Calculate mean of math_grade
mean_grade = students['math_grade'].mean()
print("Task 4 - Central tendency measures for math grades:")
print(f"Mean math grade: {mean_grade:.2f}")

# Task 4: Calculate median of math_grade
median_grade = students['math_grade'].median()
print(f"Median math grade: {median_grade}")

# Task 5: Calculate the mode of math_grade
mode_grade = students['math_grade'].mode()[0]
print(f"Mode math grade: {mode_grade}")
print()

# Task 6: Calculate the range of math_grade
range_grade = students['math_grade'].max() - students['math_grade'].min()
print("Task 5 - Variability measures for math grades:")
print(f"Range of math grade: {range_grade}")

# Task 7: Calculate standard deviation of math_grade
std_dev_grade = students['math_grade'].std()
print(f"Standard deviation of math grade: {std_dev_grade:.2f}")

# Task 8: Calculate MAD of math_grade
mean_math_grade = students['math_grade'].mean()
mad_grade = (students['math_grade'] - mean_math_grade).abs().mean()
print(f"Mean absolute deviation of math grade: {mad_grade:.2f}")
print()

# Task 9: Create a histogram of math grades
print("Task 6 - Creating histogram of math grades:")
sns.histplot(students['math_grade'], bins=10, kde=True)
plt.title("Histogram of Math Grades")
plt.xlabel("Math Grade")
plt.ylabel("Frequency")
plt.show()
plt.clf()

# Task 10: Create a box plot of math grades
print("Task 7 - Creating box plot of math grades:")
sns.boxplot(x=students['math_grade'])
plt.title("Box Plot of Math Grades")
plt.xlabel("Math Grade")
plt.show()
plt.clf()

# Task 11: Calculate the number of students with mothers in each job category
print("Task 8 - Mother's job analysis:")
mjob_counts = students['Mjob'].value_counts()
print("Count of students by mother's job:")
print(mjob_counts)
print()

# Task 12: Calculate a proportion of students with mothers in each job category
print("Task 9 - Mother's job proportions:")
mjob_proportions = mjob_counts / len(students)
print("Proportion of students by mother's job:")
print(mjob_proportions)
print(f"Proportion of students with mothers in health: {mjob_proportions.get('health', 0):.2%}")
print()

# Task 13: Create a bar chart of Mjob
print("Task 10 - Creating bar chart of mother's job:")
sns.countplot(x=students['Mjob'], order=mjob_counts.index)
plt.title("Distribution of Mother's Job")
plt.xlabel("Mother's Job")
plt.ylabel("Count")
plt.show()
plt.clf()

# Task 14: Create a pie chart of Mjob
print("Task 11 - Creating pie chart of mother's job:")
mjob_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Proportion of Mother's Job")
plt.ylabel("")  # Remove y-label for pie chart aesthetics
plt.show()

# Task 15: Further exploration
print("Task 12 - Additional exploratory analysis:")
print("Address distribution:")
print(students['address'].value_counts())
print()

sns.countplot(x=students['address'])
plt.title("Distribution of Address")
plt.xlabel("Address")
plt.ylabel("Count")
plt.show()
plt.clf()

print("Absences statistics:")
print(students['absences'].describe())
print()

sns.histplot(students['absences'], bins=10, kde=True)
plt.title("Histogram of Absences")
plt.xlabel("Number of Absences")
plt.ylabel("Frequency")
plt.show()
plt.clf()

print("Father's job distribution:")
fjob_counts = students['Fjob'].value_counts()
print(fjob_counts)
print()

sns.countplot(x=students['Fjob'], order=fjob_counts.index)
plt.title("Distribution of Father's Job")
plt.xlabel("Father's Job")
plt.ylabel("Count")
plt.show()