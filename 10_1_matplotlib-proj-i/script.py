from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here

# Task 3: Create figure with size 12x8
plt.figure(figsize=(12, 8))

# Task 4: Create left subplot
ax1 = plt.subplot(1, 2, 1)

# Task 6: Create x-values for months
x_values = range(len(months))

# Task 7: Plot total visits per month on left subplot
ax1.plot(x_values, visits_per_month, marker='o')

# Task 9: Label axes
ax1.set_xlabel("Month")
ax1.set_ylabel("Page Visits")

# Task 10: Set x-axis ticks
ax1.set_xticks(x_values)

# Task 11: Set x-axis tick labels to month names
ax1.set_xticklabels(months)

# Task 16: Title for left plot
ax1.set_title("Monthly Page Visits")

# Task 5: Create right subplot
ax2 = plt.subplot(1, 2, 2)

# Task 12: Plot multiple lime types on right subplot
ax2.plot(x_values, key_limes_per_month, color="green", label="Key Limes")
ax2.plot(x_values, persian_limes_per_month, color="orange", label="Persian Limes")
ax2.plot(x_values, blood_limes_per_month, color="red", label="Blood Limes")

# Task 15: Set ticks and labels for right subplot
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)

# Task 14: Add legend for lime types
ax2.legend()

# Task 9 (again): Label axes for right plot
ax2.set_xlabel("Month")
ax2.set_ylabel("Limes Sold")

# Task 16 (again): Title for right plot
ax2.set_title("Limes Sold Per Month by Type")

# Task 16 (continued): Adjust layout
plt.tight_layout()

# Task 17: Save the figure
plt.savefig("sublime_limes_sales_summary.png")

# Final show
plt.show()
