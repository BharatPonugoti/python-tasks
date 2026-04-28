import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
print("Current Folder:", os.getcwd())
print("Files here:", os.listdir())
# ==============================
# SCENARIO 1: DATA LOADING & PREPROCESSING
# ==============================

# Load dataset
df = pd.read_csv("ign.csv.csv")

# Display dataset info
print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nShape:", df.shape)

# Remove unnecessary column
if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

# Check missing values
print("\nMissing values:\n", df[['score', 'genre', 'platform']].isnull().sum())

# Handle missing values
df['score'].fillna(df['score'].mean(), inplace=True)
df['genre'].fillna(df['genre'].mode()[0], inplace=True)

# Fix data types
df['score'] = df['score'].astype(float)
df['release_year'] = df['release_year'].astype(int)
df['release_month'] = df['release_month'].astype(int)
df['release_day'] = df['release_day'].astype(int)


# ==============================
# SCENARIO 2: LINE GRAPH (SCORE TREND)
# ==============================

yearly_scores = df.groupby('release_year')['score'].mean()

years = yearly_scores.index.to_numpy()
avg_scores = yearly_scores.values

plt.figure()
plt.plot(years, avg_scores, marker='o')
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.savefig("avg_score_trend.png")
plt.close()


# ==============================
# SCENARIO 3: FILTERING + BAR CHART
# ==============================

high_rated = df[df['score'] > 7]

platform_counts = high_rated['platform'].value_counts()
top_platforms = platform_counts.head(10)

platforms = top_platforms.index.to_numpy()
counts = top_platforms.values

plt.figure()
plt.bar(platforms, counts)
plt.xticks(rotation=45)
plt.xlabel("Platform")
plt.ylabel("Number of High Rated Games")
plt.title("Top 10 Platforms (Score > 7)")
plt.savefig("top_platforms_bar.png")
plt.close()


# ==============================
# SCENARIO 4: PIE CHART (GENRE DISTRIBUTION)
# ==============================

genre_counts = df['genre'].value_counts()
top_genres = genre_counts.head(5)

plt.figure()
plt.pie(top_genres.values, labels=top_genres.index, autopct='%1.1f%%')
plt.title("Top 5 Genre Distribution")
plt.savefig("genre_distribution.png")
plt.close()


# ==============================
# SCENARIO 5: ADVANCED ANALYSIS
# ==============================

# Feature Engineering
def categorize(score):
    if score >= 9:
        return "Excellent"
    elif score >= 7:
        return "Good"
    else:
        return "Average"

df['score_category'] = df['score'].apply(categorize)

# Convert editors_choice
df['editors_choice'] = df['editors_choice'].map({'Y': 1, 'N': 0})

# NumPy Analysis
yearly_avg = df.groupby('release_year')['score'].mean()
score_growth = np.diff(yearly_avg.values)

print("\nYearly Score Growth:\n", score_growth)

# Line Graph
plt.figure()
plt.plot(yearly_avg.index, yearly_avg.values, marker='o')
plt.title("Score Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Average Score")
plt.savefig("score_trend.png")
plt.close()

# Stacked Bar Chart
category_counts = df.groupby(['release_year', 'score_category']).size().unstack(fill_value=0)
category_counts.plot(kind='bar', stacked=True)
plt.title("Score Categories per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("score_category_stacked.png")
plt.close()

# Histogram
plt.figure()
plt.hist(df['score'], bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("score_distribution.png")
plt.close()


# ==============================
# INSIGHTS
# ==============================

best_year = yearly_avg.idxmax()
print("\nYear with highest average score:", best_year)

trend_increasing = np.all(score_growth >= 0)
print("Are scores consistently increasing?", trend_increasing)

correlation = df['score'].corr(df['editors_choice'])
print("Correlation between score and editor's choice:", correlation)