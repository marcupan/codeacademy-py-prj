# import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binomtest

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart)
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# Task 1: Cholesterol values for patients with heart disease
chol_hd = yes_hd.chol

# Task 2: Mean cholesterol for heart disease patients
mean_chol_hd = np.mean(chol_hd)
print("Mean cholesterol (heart disease):", mean_chol_hd)

# Task 3-4: Hypothesis test - is mean chol significantly > 240?
tstat_hd, pval_hd_two_sided = ttest_1samp(chol_hd, 240)
pval_hd_one_sided = pval_hd_two_sided / 2
print("One-sided p-value (heart disease):", pval_hd_one_sided)
if pval_hd_one_sided < 0.05:
    print("Conclusion: Significantly greater than 240 mg/dl.")
else:
    print("Conclusion: Not significantly greater than 240 mg/dl.")

# Task 5: Repeat for patients without heart disease
chol_no_hd = no_hd.chol
mean_chol_no_hd = np.mean(chol_no_hd)
print("Mean cholesterol (no heart disease):", mean_chol_no_hd)

tstat_no_hd, pval_no_hd_two_sided = ttest_1samp(chol_no_hd, 240)
pval_no_hd_one_sided = pval_no_hd_two_sided / 2
print("One-sided p-value (no heart disease):", pval_no_hd_one_sided)
if pval_no_hd_one_sided < 0.05:
    print("Conclusion: Significantly greater than 240 mg/dl.")
else:
    print("Conclusion: Not significantly greater than 240 mg/dl.")

# Task 6: Total number of patients
num_patients = heart.shape[0]
print("Total patients:", num_patients)

# Task 7: Number of patients with fasting blood sugar > 120
num_highfbs_patients = heart[heart.fbs == 1].shape[0]
print("Patients with fbs > 120:", num_highfbs_patients)

# Task 8: Expected number with high fbs if 8% of pop has diabetes
expected_diabetes = num_patients * 0.08
print("Expected number with fbs > 120 (8%):", expected_diabetes)

# Task 9-10: Hypothesis test for fbs rate > 8%
pval_fbs = binomtest(num_highfbs_patients, n=num_patients, p=0.08, alternative='greater').pvalue
print("P-value for fbs > 120 test:", pval_fbs)
if pval_fbs < 0.05:
    print("Conclusion: Significantly greater than 8%")
else:
    print("Conclusion: Not significantly greater than 8%")