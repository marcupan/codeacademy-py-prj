medical_data = \
    """Marina Allison   ,27   ,   31.1 , 
    #7010.0   ;Markus Valdez   ,   30, 
    22.4,   #4050.0 ;Connie Ballard ,43 
    ,   25.3 , #12060.0 ;Darnell Weber   
    ,   35   , 20.6   , #7500.0;
    Sylvie Charles   ,22, 22.1 
    ,#3022.0   ;   Vinay Padilla,24,   
    26.9 ,#4620.0 ;Meredith Santiago, 51   , 
    29.3 ,#16330.0;   Andre Mccarty, 
    19,22.7 , #2900.0 ; 
    Lorena Hodson ,65, 33.1 , #19370.0; 
    Isaac Vu ,34, 24.8,   #7045.0"""

# 2. Replace '#' with '$'
updated_medical_data = medical_data.replace('#', '$')

# 3. Count the number of medical records
num_records = 0
for char in updated_medical_data:
    if char == '$':
        num_records += 1

print(f"There are {num_records} medical records in the data.")

# 6. Split the data into individual records
medical_data_split = updated_medical_data.split(';')

# 7. Split each record into its own list
medical_records = []
for record in medical_data_split:
    medical_records.append(record.split(','))

# 9. Clean up the data
medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

print(medical_records_clean)

# 14. Print the names of individuals in uppercase
for record in medical_records_clean:
    print(record[0].upper())

# 16. Separate data into lists
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(int(record[1]))
    bmis.append(float(record[2]))
    insurance_costs.append(float(record[3].replace('$', '')))

print("Names:", names)
print("Ages:", ages)
print("BMIs:", bmis)
print("Insurance Costs:", insurance_costs)

# 19. Calculate the average BMI
total_bmi = 0
for bmi in bmis:
    total_bmi += bmi

average_bmi = total_bmi / len(bmis)
print(f"Average BMI: {average_bmi:.2f}")

# Extra 1: Calculate the average insurance cost
total_insurance_cost = sum(insurance_costs)
average_insurance_cost = total_insurance_cost / len(insurance_costs)
print(f"Average Insurance Cost: ${average_insurance_cost:.2f}")

# Extra 2: Write detailed information for each individual
for i in range(len(names)):
    print(
        f"{names[i]} is {ages[i]} years old with a BMI of {bmis[i]:.1f} and an insurance cost of ${insurance_costs[i]:,.2f}.")
