import pandas as pd

# Task 1: Load the data into a DataFrame
inventory = pd.read_csv('inventory.csv')

# Task 2: Inspect the first 10 rows
print(inventory.head(10))

# Task 3: Save the first 10 rows (Staten Island location) to staten_island
staten_island = inventory.head(10)

# Task 4: Select product_description from staten_island
product_request = staten_island['product_description']

# Task 5: Select rows where location is Brooklyn and product_type is seeds
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

# Task 6: Add a column in_stock (True if quantity > 0, False otherwise)
inventory['in_stock'] = inventory['quantity'] > 0

# Task 7: Add a column total_value (price * quantity)
inventory['total_value'] = inventory['price'] * inventory['quantity']

# Task 8: Paste the lambda function
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

# Task 9: Add a column full_description using combine_lambda
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory)
