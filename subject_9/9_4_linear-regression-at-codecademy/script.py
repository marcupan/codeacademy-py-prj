import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

codecademy = pd.read_csv('codecademy.csv')

# Task 1: Print the first five rows
print(codecademy.head())

# Task 2: Create a scatter plot of score vs. completed
plt.scatter(codecademy['completed'], codecademy['score'])
plt.xlabel("Completed Lessons")
plt.ylabel("Quiz Score")
plt.title("Quiz Score vs Completed Lessons")
plt.show()
plt.clf()

# Task 3: Fit a linear regression to predict score based on prior lessons completed
X = sm.add_constant(codecademy['completed'])
y = codecademy['score']
model = sm.OLS(y, X).fit()
print(model.params)

# Task 4:
# Intercept interpretation: When 0 lessons are completed, the expected quiz score is approximately the intercept value.
# Slope interpretation: For each additional completed lesson, the quiz score increases by approximately the slope value.

# Task 5: Plot the scatter plot with the regression line
plt.scatter(codecademy['completed'], codecademy['score'])
plt.plot(codecademy['completed'], model.fittedvalues, color='red')
plt.xlabel("Completed Lessons")
plt.ylabel("Quiz Score")
plt.title("Regression Line over Scatter Plot")
plt.show()
plt.clf()

# Task 6: Predict score for learner who has completed 20 prior lessons
predicted_score = model.predict([1, 20])[0]
print(f"Predicted score for 20 lessons completed: {predicted_score}")

# Task 7: Calculate fitted values
fitted_values = model.fittedvalues

# Task 8: Calculate residuals
residuals = y - fitted_values

# Task 9: Check a normality assumption
plt.hist(residuals, bins=20, edgecolor='black')
plt.xlabel("Residuals")
plt.title("Histogram of Residuals")
plt.show()
plt.clf()

# Task 10: Check a homoscedasticity assumption
plt.scatter(fitted_values, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values")
plt.show()
plt.clf()

# Task 11: Create a boxplot of score vs. lesson
sns.boxplot(x='lesson', y='score', data=codecademy)
plt.title("Quiz Score by Lesson")
plt.show()
plt.clf()

# Task 12: Fit a linear regression to predict the score based on which lesson they took
codecademy['lesson_B'] = (codecademy['lesson'] == 'Lesson B').astype(int)
X_lesson = sm.add_constant(codecademy['lesson_B'])
model_lesson = sm.OLS(codecademy['score'], X_lesson).fit()
print(model_lesson.params)

# Task 13: Calculate and print the group means and mean difference
lesson_means = codecademy.groupby('lesson')['score'].mean()
print("Mean scores by lesson:")
print(lesson_means)
mean_difference = lesson_means['Lesson B'] - lesson_means['Lesson A']
print(f"Mean difference (Lesson B - Lesson A): {mean_difference}")

# Task 14: Use sns.lmplot() to plot score vs. completed colored by a lesson
sns.lmplot(x='completed', y='score', hue='lesson', data=codecademy)
plt.title("Score vs Completed by Lesson")
plt.show()
