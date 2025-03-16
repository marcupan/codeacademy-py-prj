from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import os

print(os.getcwd())

# Task 1: Load in the Spotify dataset
spotify_data = pd.read_csv('genres_v2.csv')

# Task 2: Preview the dataset
print(spotify_data.head())

# Task 3: Select the relevant column (tempo)
song_tempos = spotify_data["tempo"]

# Task 5: Plot the population distribution with the mean labeled
population_distribution(song_tempos)

# Task 6: Sampling distribution of the sample mean (sample size = 30)
sampling_distribution(song_tempos, samp_size=30, stat="Mean")

# Task 8: Sampling distribution of the sample minimum (sample size = 30)
sampling_distribution(song_tempos, samp_size=30, stat="Minimum")

# Task 10: Sampling distribution of the sample variance (sample size = 30)
sampling_distribution(song_tempos, samp_size=30, stat="Variance")

# Task 13: Calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)
print(f"Population Mean: {population_mean}")
print(f"Population Standard Deviation: {population_std}")

# Task 14: Calculate the standard error
sample_size = 30
standard_error = population_std / np.sqrt(sample_size)
print(f"Standard Error: {standard_error}")

# Task 15: Probability of observing an average tempo of 140 bpm or lower
prob_140_or_lower = stats.norm.cdf(140, loc=population_mean, scale=standard_error)
print(f"Probability of sample mean ≤ 140 bpm: {prob_140_or_lower:.4f}")

# Task 16: Probability of observing an average tempo of 150 bpm or higher
prob_150_or_higher = 1 - stats.norm.cdf(150, loc=population_mean, scale=standard_error)
print(f"Probability of sample mean ≥ 150 bpm: {prob_150_or_higher:.4f}")

# EXTRA: Exploring additional statistical properties
# You can add custom statistics to choose_statistic() in helper_functions.py
