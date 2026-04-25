# ============================================
# Project: Railway Gauges Analysis
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# ============================================
# Scenario 1: Data Loading & Cleaning
# ============================================

file_path = "railway_gauges.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("❌ File not found. Make sure 'railway_gauges.csv' is in this folder.")
    exit()

print("✅ File found")

# Load dataset
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.title()

# Display data
print("\nFirst 5 Rows:\n", df.head())
print("\nColumn Names:\n", df.columns)

# Handle missing values
df.fillna(0, inplace=True)

# Convert columns to numeric
for col in ['Broad', 'Metre', 'Narrow', 'Total']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

print("\nCleaned Data:\n", df.head())


# ============================================
# Scenario 2: Line Chart (Total Growth)
# ============================================

plt.figure()
plt.plot(df['Year'], df['Total'], marker='o')

plt.title("Total Railway Track Growth")
plt.xlabel("Year")
plt.ylabel("Total Track Length")

plt.grid()
plt.show()

# Trend analysis
if df['Total'].iloc[-1] > df['Total'].iloc[0]:
    print("\nTrend: Increasing")
else:
    print("\nTrend: Decreasing")


# ============================================
# Scenario 3: Bar Chart (After 2000)
# ============================================

df_recent = df[df['Year'] > 2000]

x = np.arange(len(df_recent))
width = 0.25

plt.figure()

plt.bar(x - width, df_recent['Broad'], width, label='Broad')
plt.bar(x, df_recent['Metre'], width, label='Metre')
plt.bar(x + width, df_recent['Narrow'], width, label='Narrow')

plt.xticks(x, df_recent['Year'])

plt.title("Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend()
plt.show()

# Dominant gauge
dominant = df_recent[['Broad', 'Metre', 'Narrow']].mean().idxmax()
print("\nDominant Gauge (After 2000):", dominant)


# ============================================
# Scenario 4: Pie Chart (Contribution)
# ============================================

totals = df[['Broad', 'Metre', 'Narrow']].sum()

plt.figure()
plt.pie(totals, labels=totals.index, autopct='%1.1f%%')

plt.title("Gauge Contribution")
plt.show()

print("\nHighest Contribution:", totals.idxmax())


# ============================================
# Scenario 5: Advanced Analysis
# ============================================

# Percentage columns
df['% Broad'] = (df['Broad'] / df['Total']) * 100
df['% Metre'] = (df['Metre'] / df['Total']) * 100
df['% Narrow'] = (df['Narrow'] / df['Total']) * 100

# Growth calculation
growth = np.diff(df['Total'])
max_growth_year = df['Year'].iloc[np.argmax(growth) + 1]

print("\nYear with Highest Growth:", max_growth_year)

# Line graph (all gauges)
plt.figure()
plt.plot(df['Year'], df['Broad'], label='Broad')
plt.plot(df['Year'], df['Metre'], label='Metre')
plt.plot(df['Year'], df['Narrow'], label='Narrow')

plt.title("Gauge Trends Over Time")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend()
plt.grid()
plt.show()

# Stacked bar chart
plt.figure()

plt.bar(df['Year'], df['Broad'], label='Broad')
plt.bar(df['Year'], df['Metre'], bottom=df['Broad'], label='Metre')
plt.bar(df['Year'], df['Narrow'], bottom=df['Broad'] + df['Metre'], label='Narrow')

plt.title("Gauge Composition Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend()
plt.show()

# Decline detection
if df['Metre'].iloc[-1] < df['Metre'].iloc[0]:
    print("Metre Gauge is Declining")

if df['Narrow'].iloc[-1] < df['Narrow'].iloc[0]:
    print("Narrow Gauge is Declining")


# ============================================
# Final Conclusion
# ============================================

if dominant == 'Broad':
    print("\nConclusion: The railway system is shifting towards Broad Gauge dominance.")
else:
    print("\nConclusion: No single gauge is fully dominant yet.")