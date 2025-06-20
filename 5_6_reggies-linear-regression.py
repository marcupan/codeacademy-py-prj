# Task 1: Define get_y function
def get_y(m, b, x):
    return m * x + b


# Testing Task 1
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


# Task 2 & 3: Define calculate_error function
def calculate_error(m, b, point):
    x_point, y_point = point
    y_on_line = get_y(m, b, x_point)
    return abs(y_on_line - y_point)


# Testing Task 4
print(calculate_error(1, 0, (3, 3)) == 0)
print(calculate_error(1, 0, (3, 4)) == 1)
print(calculate_error(1, -1, (3, 3)) == 1)
print(calculate_error(-1, 1, (3, 3)) == 5)


# Task 5: Define calculate_all_error function
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error


# Testing Task 6
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints) == 0)
print(calculate_all_error(1, 1, datapoints) == 4)
print(calculate_all_error(1, -1, datapoints) == 4)
print(calculate_all_error(-1, 1, datapoints) == 18)

# Task 8 & 9: Create possible_ms and possible_bs
possible_ms = [i / 10 for i in range(-100, 101)]
possible_bs = [i / 10 for i in range(-200, 201)]

# Task 10: Initialize variables
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

# Task 11: Find the best m and b
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            smallest_error = error
            best_m = m
            best_b = b

# Task 12: Print the results
print("Best m:", best_m)
print("Best b:", best_b)
print("Smallest error:", smallest_error)

# Task 13: Predict the bounce height for a 6cm ball
m = 0.4
b = 1.6
x = 6
print("Prediction for 6cm ball:", get_y(m, b, x))
