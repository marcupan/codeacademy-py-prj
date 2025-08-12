# Initial lists
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Task 1: Append new data
names.append("Priscilla")
insurance_costs.append(8320.0)

# Task 2: Combine names and insurance_costs into medical_records
medical_records = list(zip(insurance_costs, names))

# Task 3: Print medical_records
print("Medical Records:", medical_records)

# Task 4: Number of medical records
num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records.")

# Task 6: First medical record
first_medical_record = medical_records[0]
print(f"Here is the first medical record: {first_medical_record}")

# Task 8: Sort medical_records by insurance cost
medical_records.sort()
print(f"Here are the medical records sorted by insurance cost: {medical_records}")

# Task 9: Three cheapest insurance costs
cheapest_three = medical_records[:3]
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}")

# Task 11: Three most expensive insurance costs
priciest_three = medical_records[-3:]
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}")

# Task 13: Count occurrences of "Paul"
occurrences_paul = names.count("Paul")
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records.")

# Extra: Sort medical records alphabetically by name
alphabetical_records = sorted(medical_records, key=lambda x: x[1])
print(f"Here are the medical records sorted alphabetically by name: {alphabetical_records}")

# Extra: Middle five records
middle_five_records = medical_records[3:8]
print(f"Here are the middle five medical records: {middle_five_records}")
