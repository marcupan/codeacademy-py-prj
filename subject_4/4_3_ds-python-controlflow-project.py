# Function to analyze smoker status
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")


# Function to estimate insurance cost and provide additional advice
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
    estimated_cost = 400 * age - 128 * sex + 425 * num_of_children + 10000 * smoker - 2500
    print(f"{name}'s Estimated Insurance Cost: {estimated_cost} dollars.")
    analyze_smoker(smoker)  # Analyze smoker status
    return estimated_cost


# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name='Keanu', age=29, sex=1, num_of_children=3, smoker=1)

# Analyze your own insurance cost
my_insurance_cost = estimate_insurance_cost(name='Your Name', age=30, sex=1, num_of_children=2, smoker=0)

def test_condition(condition, true_value, false_value):
    if condition:
        return true_value
    else:
        return false_value

print(test_condition(True, 1, 2))
