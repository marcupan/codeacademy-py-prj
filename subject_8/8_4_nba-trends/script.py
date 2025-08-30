import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print("Task 1-2 - Loading and filtering NBA data:")
print(f"Total games loaded: {len(nba)}")
print(f"Games in 2010: {len(nba_2010)}")
print(f"Games in 2014: {len(nba_2014)}")
print()

# Task 1: Points scored by Knicks and Nets in 2010
knicks_pts_10 = nba_2010[nba_2010.fran_id == "Knicks"]["pts"]
nets_pts_10 = nba_2010[nba_2010.fran_id == "Nets"]["pts"]

print("Task 1 - Extracting team data for 2010:")
print(f"Knicks games in 2010: {len(knicks_pts_10)}")
print(f"Nets games in 2010: {len(nets_pts_10)}")
print()

# Task 2: Mean difference in points for 2010
diff_means_2010 = knicks_pts_10.mean() - nets_pts_10.mean()
print("Task 2 - Comparing team performance in 2010:")
print(f"Knicks average points: {knicks_pts_10.mean():.2f}")
print(f"Nets average points: {nets_pts_10.mean():.2f}")
print(f"Mean difference (Knicks - Nets): {diff_means_2010:.2f}")
print()

# Task 3: Overlapping histograms for Knicks and Nets in 2010
print("Task 3 - Creating overlapping histograms for 2010:")
plt.figure(figsize=(10, 6))
plt.hist(knicks_pts_10, alpha=0.5, label="Knicks", bins=5, color='blue')
plt.hist(nets_pts_10, alpha=0.5, label="Nets", bins=5, color='red')
plt.legend()
plt.title("Knicks vs Nets Points Distribution in 2010")
plt.xlabel("Points Scored")
plt.ylabel("Frequency")
plt.show()
plt.clf()

# Task 4: Mean difference and histograms for 2014
knicks_pts_14 = nba_2014[nba_2014.fran_id == "Knicks"]["pts"]
nets_pts_14 = nba_2014[nba_2014.fran_id == "Nets"]["pts"]

diff_means_2014 = knicks_pts_14.mean() - nets_pts_14.mean()
print("Task 4 - Comparing team performance in 2014:")
print(f"Knicks average points: {knicks_pts_14.mean():.2f}")
print(f"Nets average points: {nets_pts_14.mean():.2f}")
print(f"Mean difference (Knicks - Nets): {diff_means_2014:.2f}")
print()

print("Creating overlapping histograms for 2014:")
plt.figure(figsize=(10, 6))
plt.hist(knicks_pts_14, alpha=0.5, label="Knicks", bins=5, color='blue')
plt.hist(nets_pts_14, alpha=0.5, label="Nets", bins=5, color='red')
plt.legend()
plt.title("Knicks vs Nets Points Distribution in 2014")
plt.xlabel("Points Scored")
plt.ylabel("Frequency")
plt.show()
plt.clf()

# Task 5: Boxplots for all teams in 2010
print("Task 5 - Creating boxplot for all teams in 2010:")
plt.figure(figsize=(15, 8))
sns.boxplot(data=nba_2010, x="fran_id", y="pts")
plt.title("Points Scored per Game by Team (2010)")
plt.xlabel("Team")
plt.ylabel("Points")
plt.xticks(rotation=45)
plt.show()
plt.clf()

# Task 6: Contingency table for game results and location
location_result_freq = pd.crosstab(nba_2010["game_location"], nba_2010["game_result"])
print("Task 6 - Contingency table (game location vs result):")
print(location_result_freq)
print()

# Task 7: Table of proportions
location_result_proportions = location_result_freq.div(location_result_freq.sum(axis=1), axis=0)
print("Task 7 - Proportions table (home advantage analysis):")
print(location_result_proportions)
print(f"Home win rate: {location_result_proportions.loc['H', 'W']:.2%}")
print(f"Away win rate: {location_result_proportions.loc['A', 'W']:.2%}")
print()

# Task 8: Chi-Square test
chi2, p, dof, expected = chi2_contingency(location_result_freq)
print("Task 8 - Chi-Square independence test:")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of Freedom: {dof}")
print("Expected frequencies if independent:")
print(expected)
print(f"Significant relationship: {'Yes' if p < 0.05 else 'No'} (α = 0.05)")
print()

# Task 9: Covariance between forecast and point_diff
point_diff_forecast_cov = nba_2010["forecast"].cov(nba_2010["point_diff"])
print("Task 9 - Relationship analysis between forecast and actual performance:")
print(f"Covariance (forecast vs point difference): {point_diff_forecast_cov:.4f}")

# Task 10: Correlation between forecast and point_diff
point_diff_forecast_corr = nba_2010["forecast"].corr(nba_2010["point_diff"])
print(f"Correlation (forecast vs point difference): {point_diff_forecast_corr:.4f}")
print()

# Task 11: Scatter plot of forecast vs. point_diff
print("Task 10-11 - Creating scatter plot for forecast accuracy:")
plt.figure(figsize=(10, 6))
plt.scatter(nba_2010["forecast"], nba_2010["point_diff"], alpha=0.6)
plt.title("Forecasted Win Probability vs Actual Point Difference (2010)")
plt.xlabel("Forecasted Win Probability")
plt.ylabel("Point Difference")
plt.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Tie game')
plt.axvline(x=0.5, color='green', linestyle='--', alpha=0.5, label='50% win probability')
plt.legend()
plt.show()

print("\nAnalysis Summary:")
print(f"1. Team Comparison: Knicks vs Nets changed from {diff_means_2010:.1f} to {diff_means_2014:.1f} point difference")
print(f"2. Home Advantage: Teams win {location_result_proportions.loc['H', 'W']:.1%} at home vs {location_result_proportions.loc['A', 'W']:.1%} away")
print(f"3. Forecast Accuracy: Correlation of {point_diff_forecast_corr:.3f} between predictions and actual results")