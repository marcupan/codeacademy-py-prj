import pandas as pd

# Display full column contents with a large integer value
pd.set_option('display.max_colwidth', -1)

# Load the data
jeopardy = pd.read_csv('jeopardy.csv')

print("head: ", jeopardy.head())

# Task 2: Inspect the data
print("Columns before renaming:", jeopardy.columns)
jeopardy.rename(columns=lambda x: x.strip(), inplace=True)
print("Columns after renaming:", jeopardy.columns)

# Task 3: Function to filter questions based on a list of words
def filter_questions(data, words):
    filter_func = lambda x: all(word.lower() in x.lower() for word in words)
    return data[data['Question'].apply(filter_func)]

# Test filter_questions function
filtered_questions = filter_questions(jeopardy, ['King', 'England'])
print(filtered_questions['Question'])

# Task 4: Improve robustness of filter_questions
def filter_questions_robust(data, words):
    filter_func = lambda x: all(f" {word.lower()} " in f" {x.lower()} " for word in words)
    return data[data['Question'].apply(filter_func)]

# Test improved function
filtered_questions_robust = filter_questions_robust(jeopardy, ['King', 'England'])
print(filtered_questions_robust['Question'])

# Task 5: Convert "Value" column to floats and analyze difficulty
def clean_value(value):
    # Replace unwanted strings and convert to float
    if isinstance(value, str):
        value = value.replace('$', '').replace(',', '')
        if value == 'no value':
            return 0
    try:
        return float(value)
    except ValueError:
        return 0

jeopardy['Float Value'] = jeopardy['Value'].apply(clean_value)
filtered_king = filter_questions_robust(jeopardy, ['King'])
average_value_king = filtered_king['Float Value'].mean()
print(f"Average value of questions containing 'King': {average_value_king}")

# Task 6: Count unique answers
def count_unique_answers(data):
    return data['Answer'].value_counts()

unique_answers = count_unique_answers(filtered_king)
print(unique_answers)

# Task 7: Explore further
# Example 1: Questions about "Computer" from the 90s vs 2000s
jeopardy['Air Date'] = pd.to_datetime(jeopardy['Air Date'])
questions_90s = filter_questions_robust(jeopardy[jeopardy['Air Date'].dt.year.between(1990, 1999)], ['Computer'])
questions_2000s = filter_questions_robust(jeopardy[jeopardy['Air Date'].dt.year.between(2000, 2009)], ['Computer'])
print(f"Questions about 'Computer' in the 90s: {len(questions_90s)}")
print(f"Questions about 'Computer' in the 2000s: {len(questions_2000s)}")

# Example 2: Connection between round and category
round_category_counts = jeopardy.groupby(['Round', 'Category']).size().reset_index(name='Count')
print(round_category_counts)

# Example 3: Build a self-quizzing system
import random

def quiz_user(data):
    random_question = data.sample(1).iloc[0]
    print(f"Question: {random_question['Question']}")
    user_answer = input("Your answer: ")
    if user_answer.lower() == random_question['Answer'].lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was: {random_question['Answer']}")

# Uncomment to run the quiz
# quiz_user(jeopardy)
