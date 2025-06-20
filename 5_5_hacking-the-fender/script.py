import csv  # Task 1: Import the CSV module to handle CSV files
import json  # Task 13: Import the JSON module to handle JSON data

# Task 2: Create a list to store usernames of compromised accounts
compromised_users = []

# Task 3: Open the "passwords.csv" file and parse it using csv.DictReader
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)

    # Task 4: Iterate through each row of the CSV file
    for password_row in password_csv:
        # Task 5: Append the "Username" column to the compromised_users list
        compromised_users.append(password_row['Username'])

# Task 6: Exit the with block for "passwords.csv" (file is automatically closed)

# Task 7: Open a new file "compromised_users.txt" in write mode
with open('compromised_users.txt', 'w') as compromised_user_file:
    # Task 8: Write each username from the compromised_users list to the file
    for user in compromised_users:
        compromised_user_file.write(user + '\n')

# Task 9: Exit the with block for "compromised_users.txt" (file is automatically closed)

# Task 10: Open a JSON file called "boss_message.json" in write mode
with open('boss_message.json', 'w') as boss_message:
    # Task 11: Create a dictionary with a message for the boss
    boss_message_dict = {
        "recipient": "The Boss",  # Task 12: Add "recipient" key with value "The Boss"
        "message": "Mission Success"  # Task 12: Add "message" key with value "Mission Success"
    }
    # Task 14: Write the dictionary to the JSON file using json.dump
    json.dump(boss_message_dict, boss_message)

# Task 15: Exit the with block for "boss_message.json" (file is automatically closed)

# Task 16: Define Slash Null's signature as a multi-line string
slash_null_sig = """
 _  _     ___   __  ____
/ )( \   / __) /  \(_  _)
) \/ (  ( (_ \(  O ) )(
\____/   \___/ \__/ (__)
 _  _   __    ___  __ _  ____  ____
/ )( \ / _\  / __)(  / )(  __)(    \
) __ (/    \( (__  )  (  ) _)  ) D (
\_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _
 ___   / ___)(  )   / _\ / ___)/ )( \\
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __
(  ( \/ )( \(  )  (  )
/    /) \/ (/ (_/\/ (_/\
\_)__)\____/\____/\____/
"""

# Task 17: Open a file called "new_passwords.csv" in write mode
with open('new_passwords.csv', 'w') as new_passwords_obj:
    # Task 18: Write Slash Null's signature to the new_passwords file
    new_passwords_obj.write(slash_null_sig)

# Task 19: Exit the with block for "new_passwords.csv" (file is automatically closed)

# Final step: Print a success message
print("All tasks completed successfully!")
