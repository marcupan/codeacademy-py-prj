import pandas as pd

# Load the data
ad_clicks = pd.read_csv('ad_clicks.csv')

# Task 1: Examine the first few rows
print(ad_clicks.head())

# Task 2: Count views from each utm_source
views_by_source = ad_clicks['utm_source'].value_counts()
print(views_by_source)

# Task 3: Create a new column is_click
ad_clicks['is_click'] = ~ad_clicks['ad_click_timestamp'].isnull()
print(ad_clicks.head())

# Task 4: Group by utm_source and is_click
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

# Task 5: Pivot the data
clicks_pivot = clicks_by_source.pivot(
    index='utm_source',
    columns='is_click',
    values='user_id'
).reset_index()
clicks_pivot.columns = ['utm_source', 'not_clicked', 'clicked']
print(clicks_pivot)

# Task 6: Add percent_clicked column
clicks_pivot['percent_clicked'] = clicks_pivot['clicked'] / (clicks_pivot['clicked'] + clicks_pivot['not_clicked'])
print(clicks_pivot)

# Task 7: Count users in experimental_group
group_counts = ad_clicks['experimental_group'].value_counts()
print(group_counts)

# Task 8: Compare click rates between Ad A and Ad B
clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
clicks_by_group_pivot = clicks_by_group.pivot(
    index='experimental_group',
    columns='is_click',
    values='user_id'
).reset_index()
clicks_by_group_pivot.columns = ['experimental_group', 'not_clicked', 'clicked']
clicks_by_group_pivot['percent_clicked'] = clicks_by_group_pivot['clicked'] / (
        clicks_by_group_pivot['clicked'] + clicks_by_group_pivot['not_clicked']
)
print(clicks_by_group_pivot)

# Task 9: Split data into A and B groups
a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']

# Task 10: Calculate percent of users who clicked by day for each group
a_clicks_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
a_clicks_pivot = a_clicks_by_day.pivot(
    index='day',
    columns='is_click',
    values='user_id'
).reset_index()
a_clicks_pivot.columns = ['day', 'not_clicked', 'clicked']
a_clicks_pivot['percent_clicked'] = a_clicks_pivot['clicked'] / (
        a_clicks_pivot['clicked'] + a_clicks_pivot['not_clicked']
)
print(a_clicks_pivot)

b_clicks_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
# Pivot and explicitly add missing columns
b_clicks_pivot = b_clicks_by_day.pivot(
    index='day',
    columns='is_click',
    values='user_id'
).reset_index()

# Rename columns, ensuring default structure
b_clicks_pivot = b_clicks_pivot.rename(columns={False: 'not_clicked', True: 'clicked'})

# Add missing columns if necessary
if 'not_clicked' not in b_clicks_pivot.columns:
    b_clicks_pivot['not_clicked'] = 0
if 'clicked' not in b_clicks_pivot.columns:
    b_clicks_pivot['clicked'] = 0

# Fill NaN values with 0
b_clicks_pivot = b_clicks_pivot.fillna(0)

# Calculate percent_clicked
b_clicks_pivot['percent_clicked'] = b_clicks_pivot['clicked'] / (
        b_clicks_pivot['clicked'] + b_clicks_pivot['not_clicked']
)

print(b_clicks_pivot)

# Task 11: Compare A and B results and decide the better ad
print("Ad A Click Rates by Day:")
print(a_clicks_pivot)
print("Ad B Click Rates by Day:")
print(b_clicks_pivot)
