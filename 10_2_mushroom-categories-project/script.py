import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Task 1: Load the data and preview
# (Inspect first five rows to understand structure)
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# Task 2: Get list of all column headers
columns = df.columns.tolist()

# Task 3, 8: Loop through columns, plot countplot ordered by descending frequency
for column in columns:
    # (Uncomment to verify loop)  # Task 2
    # print(column)

    sns.countplot(
        data=df,
        x=column,
        order=df[column].value_counts().index  # Task 8: order bars by count
    )

    # Task 6: Rotate x-tick labels and increase font size
    plt.xticks(rotation=30, fontsize=10)
    plt.xlabel(column, fontsize=12)

    # Task 7: Add informative title
    plt.title(f"{column} Value Counts")

    # Task 4: Show plot then clear for next
    plt.show()
    plt.clf()
