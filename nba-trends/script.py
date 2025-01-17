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

# Task 1: Points scored by Knicks and Nets in 2010
knicks_pts_10 = nba_2010[nba_2010.fran_id == "Knicks"]["pts"]
nets_pts_10 = nba_2010[nba_2010.fran_id == "Nets"]["pts"]

# Task 2: Mean difference in points for 2010
diff_means_2010 = knicks_pts_10.mean() - nets_pts_10.mean()
print(f"Mean difference in 2010: {diff_means_2010}")

# Task 3: Overlapping histograms for Knicks and Nets in 2010
plt.hist(knicks_pts_10, alpha=0.5, label="Knicks", bins=5)
plt.hist(nets_pts_10, alpha=0.5, label="Nets", bins=5)
plt.legend()
plt.title("Knicks vs Nets Points in 2010")
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.show()
plt.clf()

# Task 4: Mean difference and histograms for 2014
knicks_pts_14 = nba_2014[nba_2014.fran_id == "Knicks"]["pts"]
nets_pts_14 = nba_2014[nba_2014.fran_id == "Nets"]["pts"]

diff_means_2014 = knicks_pts_14.mean() - nets_pts_14.mean()
print(f"Mean difference in 2014: {diff_means_2014}")

plt.hist(knicks_pts_14, alpha=0.5, label="Knicks", bins=5)
plt.hist(nets_pts_14, alpha=0.5, label="Nets", bins=5)
plt.legend()
plt.title("Knicks vs Nets Points in 2014")
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.show()
plt.clf()

# Task 5: Boxplots for all teams in 2010
sns.boxplot(data=nba_2010, x="fran_id", y="pts")
plt.title("Points Scored per Game by Team (2010)")
plt.xlabel("Team")
plt.ylabel("Points")
plt.show()
plt.clf()

# Task 6: Contingency table for game results and location
location_result_freq = pd.crosstab(nba_2010["game_location"], nba_2010["game_result"])
print(location_result_freq)

# Task 7: Table of proportions
location_result_proportions = location_result_freq.div(location_result_freq.sum(axis=1), axis=0)
print(location_result_proportions)

# Task 8: Chi-Square test
chi2, p, dof, expected = chi2_contingency(location_result_freq)
print(f"Chi-Square Statistic: {chi2}")
print("Expected Table:")
print(expected)

# Task 9: Covariance between forecast and point_diff
point_diff_forecast_cov = nba_2010["forecast"].cov(nba_2010["point_diff"])
print(f"Covariance: {point_diff_forecast_cov}")

# Task 10: Correlation between forecast and point_diff
point_diff_forecast_corr = nba_2010["forecast"].corr(nba_2010["point_diff"])
print(f"Correlation: {point_diff_forecast_corr}")

# Task 11: Scatter plot of forecast vs point_diff
plt.scatter(nba_2010["forecast"], nba_2010["point_diff"])
plt.title("Forecast vs Point Difference (2010)")
plt.xlabel("Forecasted Win Probability")
plt.ylabel("Point Difference")
plt.show()
