# Function to estimate insurance cost
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print(f"{name}'s Estimated Insurance Cost: {estimated_cost} dollars.")
    return estimated_cost


# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name="Maria", age=31, sex=0, bmi=23.1, num_of_children=1, smoker=0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name="Rohan", age=25, sex=1, bmi=28.5, num_of_children=3, smoker=0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name="Valentina", age=53, sex=0, bmi=31.4, num_of_children=0,
                                                   smoker=1)

# Task 2: Create a list of names
names = ["Maria", "Rohan", "Valentina"]

# Task 3: Create a list of actual insurance costs
insurance_costs = [4150.0, 5320.0, 35210.0]

# Task 4: Combine names and insurance costs into insurance_data
insurance_data = zip(names, insurance_costs)

# Task 5: Convert insurance_data to a list
insurance_data = list(insurance_data)

# Task 6: Create an empty list for estimated insurance data
estimated_insurance_data = []

# Task 7: Append estimated insurance data to the list
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

# Task 8: Print the lists with clear messages
print("Here is the actual insurance cost data:", insurance_data)
print("Here is the estimated insurance cost data:", estimated_insurance_data)

# Extra: Calculate the difference between actual and estimated costs
insurance_cost_difference = [
    actual - estimated for (_, actual), (_, estimated) in zip(insurance_data, estimated_insurance_data)
]
print("Differences between actual and estimated insurance costs:", insurance_cost_difference)

# Extra: Estimate insurance cost for Akira and update lists
akira_insurance_cost = estimate_insurance_cost(name="Akira", age=19, sex=1, bmi=27.1, num_of_children=0, smoker=0)
names.append("Akira")
insurance_costs.append(2930.0)
insurance_data = list(zip(names, insurance_costs))
estimated_insurance_data.append(("Akira", akira_insurance_cost))

# Print updated data
print("Updated actual insurance cost data:", insurance_data)
print("Updated estimated insurance cost data:", estimated_insurance_data)


test_keys = ["key_1", "key_2", "key_3"]
test_values = [1, 2, 3]
test_zip = zip(test_keys, test_values)
test_zip_2 = zip(test_keys, test_values)
print("test_zip: ", test_zip)
test_dict = dict(test_zip)
print("test_dict: ", test_dict)
test_list = list(test_zip_2)
print("test_list: ", test_list)
test_list.append(("key_3", 3))
print("test_list: ", test_list)

def test_named_props(keys, values):
    zip_obj = zip(keys, values)
    return dict(zip_obj)

test_named_props_dict = test_named_props(test_keys, test_values)
print(test_named_props(test_keys, test_values))

test_conditional_list_comp = sum([value for value in test_named_props_dict.values() if value > 1])
test_multiply_list_comp = [value * 2 for key, value in test_named_props_dict.items()]
print(test_conditional_list_comp, test_multiply_list_comp)
