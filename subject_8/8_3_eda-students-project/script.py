# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Task 1: Print first few rows of data
print(students.head())

# Task 2: Print summary statistics for all columns
print(students.describe())

# Determine if more students live in urban or rural areas
urban_count = students['address'].value_counts().get('U', 0)
rural_count = students['address'].value_counts().get('R', 0)
print(f"Urban: {urban_count}, Rural: {rural_count}")

# Task 3: Calculate mean of math_grade
mean_grade = students['math_grade'].mean()
print(f"Mean math grade: {mean_grade}")

# Task 4: Calculate median of math_grade
median_grade = students['math_grade'].median()
print(f"Median math grade: {median_grade}")

# Task 5: Calculate mode of math_grade
mode_grade = students['math_grade'].mode()[0]
print(f"Mode math grade: {mode_grade}")

# Task 6: Calculate range of math_grade
range_grade = students['math_grade'].max() - students['math_grade'].min()
print(f"Range of math grade: {range_grade}")

# Task 7: Calculate standard deviation of math_grade
std_dev_grade = students['math_grade'].std()
print(f"Standard deviation of math grade: {std_dev_grade}")

# Task 8: Calculate MAD of math_grade
mad_grade = students['math_grade'].mad()
print(f"Mean absolute deviation of math grade: {mad_grade}")

# Task 9: Create a histogram of math grades
sns.histplot(students['math_grade'], bins=10, kde=True)
plt.title("Histogram of Math Grades")
plt.xlabel("Math Grade")
plt.ylabel("Frequency")
plt.show()
plt.clf()

# Task 10: Create a box plot of math grades
sns.boxplot(x=students['math_grade'])
plt.title("Box Plot of Math Grades")
plt.xlabel("Math Grade")
plt.show()
plt.clf()

# Task 11: Calculate number of students with mothers in each job category
mjob_counts = students['Mjob'].value_counts()
print(mjob_counts)

# Task 12: Calculate proportion of students with mothers in each job category
mjob_proportions = mjob_counts / len(students)
print(mjob_proportions)
print(f"Proportion of students with mothers in health: {mjob_proportions.get('health', 0):.2%}")

# Task 13: Create a bar chart of Mjob
sns.countplot(x=students['Mjob'], order=mjob_counts.index)
plt.title("Distribution of Mother's Job")
plt.xlabel("Mother's Job")
plt.ylabel("Count")
plt.show()
plt.clf()

# Task 14: Create a pie chart of Mjob
mjob_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Proportion of Mother's Job")
plt.ylabel("")  # Remove y-label for pie chart aesthetics
plt.show()

# Task 15: Further exploration
# Summary statistics and visualizations for 'address', 'absences', 'Fjob'
print(students['address'].value_counts())
sns.countplot(x=students['address'])
plt.title("Distribution of Address")
plt.xlabel("Address")
plt.ylabel("Count")
plt.show()
plt.clf()

print(students['absences'].describe())
sns.histplot(students['absences'], bins=10, kde=True)
plt.title("Histogram of Absences")
plt.xlabel("Number of Absences")
plt.ylabel("Frequency")
plt.show()
plt.clf()

fjob_counts = students['Fjob'].value_counts()
print(fjob_counts)
sns.countplot(x=students['Fjob'], order=fjob_counts.index)
plt.title("Distribution of Father's Job")
plt.xlabel("Father's Job")
plt.ylabel("Count")
plt.show()
