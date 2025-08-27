import pandas as pd

# Load the data
visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

# Task 1: Inspect the DataFrames
print("Visits:")
print(visits.head())
print("Cart:")
print(cart.head())
print("Checkout:")
print(checkout.head())
print("Purchase:")
print(purchase.head())

# Task 2: Combine visits and cart using a left merge
visits_cart = pd.merge(visits, cart, how='left', on='user_id')

# Task 3: Length of the merged DataFrame
print("Length of visits_cart:", len(visits_cart))

# Task 4: Count null values in cart_time
null_cart_time = visits_cart['cart_time'].isnull().sum()
print("Null cart_time:", null_cart_time)

# Task 5: Percentage of users who visited but did not add to cart
percent_no_cart = (null_cart_time / len(visits_cart)) * 100
print("Percent of users who visited but did not add to cart:", percent_no_cart)

# Task 6: Combine cart and checkout using a left merge
cart_checkout = pd.merge(cart, checkout, how='left', on='user_id')
null_checkout_time = cart_checkout['checkout_time'].isnull().sum()
percent_no_checkout = (null_checkout_time / len(cart_checkout)) * 100
print("Percent of users who added to cart but did not proceed to checkout:", percent_no_checkout)

# Task 7: Merge all four steps
all_data = visits.merge(cart, how='left', on='user_id') \
    .merge(checkout, how='left', on='user_id') \
    .merge(purchase, how='left', on='user_id')
print("All Data:")
print(all_data.head())

# Task 8: Percentage of users who proceeded to check out but did not purchase
null_purchase_time = all_data['purchase_time'].isnull().sum()
checkout_to_purchase = (null_purchase_time / len(all_data[~all_data['checkout_time'].isnull()])) * 100
print("Percent of users who proceeded to checkout but did not purchase:", checkout_to_purchase)

# Task 9: Identify the weakest step
print("Weakest step analysis:")
print(f"Visit to Cart Dropoff: {percent_no_cart}%")
print(f"Cart to Checkout Dropoff: {percent_no_checkout}%")
print(f"Checkout to Purchase Dropoff: {checkout_to_purchase}%")

# Task 10: Calculate the time from an initial visit to final purchase
all_data['time_to_purchase'] = all_data['purchase_time'] - all_data['visit_time']

# Task 11: Examine the new column
print("Time to Purchase:")
print(all_data['time_to_purchase'])

# Task 12: Average time to purchase
average_time_to_purchase = all_data['time_to_purchase'].mean()
print("Average time to purchase:", average_time_to_purchase)
