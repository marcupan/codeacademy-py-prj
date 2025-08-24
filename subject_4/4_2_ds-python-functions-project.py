# Create calculate_insurance_cost() function
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    message = f"The estimated insurance cost for {name} is {estimated_cost} dollars."
    return message, estimated_cost

def second_calc(name, current_year, age):
    year_of_birth = current_year - age
    message = f"{name} was born in {year_of_birth}."
    return message, year_of_birth


# Create a function to calculate the difference in insurance costs
def insurance_diff(cost1, cost2):
    difference = abs(cost1 - cost2)
    print(f"The difference in insurance cost is {difference} dollars.")


# Estimate Maria's insurance cost
maria_message, maria_insurance_cost = calculate_insurance_cost(
    name="Maria",
    age=28,
    sex=0,
    bmi=26.2,
    num_of_children=3,
    smoker=0
)
print(maria_message)

# Estimate Omar's insurance cost
omar_message, omar_insurance_cost = calculate_insurance_cost(
    name="Omar",
    age=35,
    sex=1,
    bmi=22.2,
    num_of_children=0,
    smoker=1
)
print(omar_message)

# Calculate and print the difference in insurance costs
insurance_diff(omar_insurance_cost, maria_insurance_cost)

# Estimate your own insurance cost
my_message, my_insurance_cost = calculate_insurance_cost(
    name="Your Name",
    age=30,
    sex=1,
    bmi=24.5,
    num_of_children=1,
    smoker=0
)
print(my_message)

year_of_birth_m, current_year_m = second_calc("Your Name", 2021, 30)
print(year_of_birth_m, current_year_m)
