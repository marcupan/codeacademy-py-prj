# Step 1: Create a list of paintings
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# Step 2: Create a list of dates
dates = [1939, 1933, 1946, 1940]

# Step 3: Zip together paintings and dates
paintings = list(zip(paintings, dates))
print("Paintings with dates:", paintings)

# Step 4: Append additional paintings and dates
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print("Updated paintings list:", paintings)

# Step 5: Find the length of the painting list
total_paintings = len(paintings)
print("Total number of paintings:", total_paintings)

# Step 6: Generate audio tour numbers
audio_tour_number = list(range(1, total_paintings + 1))
print("Audio tour numbers:", audio_tour_number)

# Step 7: Create the master list
master_list = list(zip(audio_tour_number, paintings))

# Step 8: Print the master list
print("Master list:")
for item in master_list:
    print(item)
