# Initial lists
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Task 1: Initialize total_cost
total_cost = 0

# Task 2: Add up all insurance costs
for cost in actual_insurance_costs:
    total_cost += cost

# Task 3: Calculate the average insurance cost
average_cost = total_cost / len(actual_insurance_costs)

# Task 4: Print average cost
print(f"Average Insurance Cost: {average_cost} dollars.")

# Task 5: Iterate through names using a range
for i in range(len(names)):
    # Task 6: Store name and insurance cost
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print(f"The insurance cost for {name} is {insurance_cost} dollars.")

    # Task 8: Check if insurance cost is above, below, or equal to average
    if insurance_cost > average_cost:
        print(f"The insurance cost for {name} is above average.")
    elif insurance_cost < average_cost:
        print(f"The insurance cost for {name} is below average.")
    else:
        print(f"The insurance cost for {name} is equal to the average.")

# Task 10: Create updated_estimated_costs using list comprehension
updated_estimated_costs = [cost * 11 / 10 for cost in estimated_insurance_costs]

# Task 11: Print updated_estimated_costs
print("Updated Estimated Costs:", updated_estimated_costs)

# Extra: Convert first for loop to a while loop
total_cost = 0
i = 0
while i < len(actual_insurance_costs):
    total_cost += actual_insurance_costs[i]
    i += 1
average_cost = total_cost / len(actual_insurance_costs)
print(f"Average Insurance Cost (calculated using while loop): {average_cost} dollars.")

# Extra: Modify second loop to calculate difference from average
for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    estimated_cost = estimated_insurance_costs[i]
    difference = insurance_cost - average_cost
    print(f"The insurance cost for {name} is {insurance_cost} dollars.")
    if insurance_cost > average_cost:
        print(f"The insurance cost for {name} is above average by {difference:.2f} dollars.")
    elif insurance_cost < average_cost:
        print(f"The insurance cost for {name} is below average by {abs(difference):.2f} dollars.")
    else:
        print(f"The insurance cost for {name} is equal to the average.")
