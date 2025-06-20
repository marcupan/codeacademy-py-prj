import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: Define the rate parameter
lam = 7

## Task 2: Probability of observing exactly lam defects
prob_exact_lam = stats.poisson.pmf(lam, lam)
print(f"Probability of exactly {lam} defects: {prob_exact_lam:.4f}")

## Task 3: Probability of 4 or fewer defects (good days)
prob_good_day = stats.poisson.cdf(4, lam)
print(f"Probability of 4 or fewer defects: {prob_good_day:.4f}")

## Task 4: Probability of more than 9 defects (bad days)
prob_bad_day = 1 - stats.poisson.cdf(9, lam)
print(f"Probability of more than 9 defects: {prob_bad_day:.4f}")

### Task Group 2 ###
## Task 5: Generate 365 days of defect data
year_defects = np.random.poisson(lam, 365)

## Task 6: Print the first 20 values
print("First 20 days of defects:", year_defects[:20])

## Task 7: Expected number of defects in a year
expected_defects_year = lam * 365
print(f"Expected defects in a year: {expected_defects_year}")

## Task 8: Sum of actual defects in the year
actual_defects_year = np.sum(year_defects)
print(f"Total defects in the year: {actual_defects_year}")

## Task 9: Average number of defects per day
average_defects = np.mean(year_defects)
print(f"Average defects per day: {average_defects:.2f}")

## Task 10: Maximum defects on a single day
max_defects = np.max(year_defects)
print(f"Maximum defects in a single day: {max_defects}")

## Task 11: Probability of observing max defects or more
prob_max_or_more = 1 - stats.poisson.cdf(max_defects - 1, lam)
print(f"Probability of {max_defects} or more defects in a day: {prob_max_or_more:.4f}")

### Extra Bonus ###
## Task 12: 90th percentile of Poisson(7)
percentile_90 = stats.poisson.ppf(0.90, lam)
print(f"90th percentile defect count: {int(percentile_90)}")

## Task 13: Proportion of dataset greater than or equal to 90th percentile
prop_above_90th = np.sum(year_defects >= percentile_90) / len(year_defects)
print(f"Proportion of days with defects >= 90th percentile: {prop_above_90th:.2f}")
