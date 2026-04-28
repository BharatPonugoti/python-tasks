# ==========================================================
# HOUSE SALES DATA ANALYSIS PROJECT (SCENARIO 1 → 5)
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================================
# SETUP
# ==========================================================

file_path = "kc_house_data.csv"
save_path = r"C:/Users/Admin/Documents/pyCodes/data_Analytics/project_4/pictorial_analysis"

# Create folder safely
os.makedirs(save_path, exist_ok=True)

# Check file exists
if not os.path.exists(file_path):
    print("ERROR: CSV file not found!")
    print("Current files:", os.listdir())
    exit()

# Load dataset
df = pd.read_csv(file_path)

print("\n===== DATA LOADED SUCCESSFULLY =====")

# ==========================================================
# SCENARIO 1: DATA CLEANING
# ==========================================================

print("\n===== SCENARIO 1: DATA CLEANING =====")

cols = ["bedrooms", "bathrooms", "sqft_living", "price"]

# Convert to numeric
for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing values
df["bedrooms"].fillna(df["bedrooms"].mode()[0], inplace=True)
df["bathrooms"].fillna(df["bathrooms"].mean(), inplace=True)
df["sqft_living"].fillna(df["sqft_living"].mean(), inplace=True)
df["price"].fillna(df["price"].mean(), inplace=True)

# Convert bedrooms to integer
df["bedrooms"] = df["bedrooms"].round().astype(int)

print("Missing values after cleaning:")
print(df[cols].isnull().sum())

# ==========================================================
# SCENARIO 2: LINE GRAPH (FIRST 10 RECORDS)
# ==========================================================

print("\n===== SCENARIO 2: LINE GRAPH =====")

subset = df[['id', 'price']].head(10)
price_array = subset['price'].to_numpy()

plt.figure(figsize=(8,5))
plt.plot(price_array, marker='o')

plt.title("House Prices (First 10 Records)")
plt.xlabel("Index (0–9)")
plt.ylabel("Price")

plt.tight_layout()
plt.savefig(os.path.join(save_path, "house_prices_line.png"))
plt.show()

# ==========================================================
# SCENARIO 3: BAR CHART (EXPENSIVE HOUSES)
# ==========================================================

print("\n===== SCENARIO 3: BAR CHART =====")

expensive = df[df["price"] > 300000]

bedroom_counts = expensive["bedrooms"].value_counts().sort_index()
top_bedrooms = bedroom_counts.head(5)

plt.figure(figsize=(8,5))
plt.bar(top_bedrooms.index, top_bedrooms.values)

plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Expensive Houses by Bedrooms")

plt.xticks(top_bedrooms.index)
plt.tight_layout()

plt.savefig(os.path.join(save_path, "expensive_houses_bar.png"))
plt.show()

# ==========================================================
# SCENARIO 4: PIE CHART
# ==========================================================

print("\n===== SCENARIO 4: PIE CHART =====")

bedroom_counts = df["bedrooms"].value_counts().head(5)

labels = [f"{b} Bedrooms" for b in bedroom_counts.index]
values = bedroom_counts.values

plt.figure(figsize=(8,6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

plt.title("Bedroom Distribution (Top 5)")
plt.axis('equal')

plt.savefig(os.path.join(save_path, "bedroom_distribution.png"))
plt.show()

# ==========================================================
# SCENARIO 5: ADVANCED ANALYSIS
# ==========================================================

print("\n===== SCENARIO 5: ADVANCED ANALYSIS =====")

# Feature creation
def categorize_price(price):
    if price >= 1000000:
        return "Luxury"
    elif price >= 500000:
        return "Mid Range"
    else:
        return "Affordable"

df["price_category"] = df["price"].apply(categorize_price)

print("\nPrice Category Counts:")
print(df["price_category"].value_counts())

# NumPy usage
price_array = df["price"].dropna().to_numpy()
price_diff = np.diff(price_array)

print("\nFirst 10 Price Differences:")
print(price_diff[:10])

# -------- Line Graph --------
plt.figure(figsize=(10,5))
plt.plot(price_array[:100], marker='o', color="green")

plt.title("House Price Trend")
plt.xlabel("Index")
plt.ylabel("Price")

plt.tight_layout()
plt.savefig(os.path.join(save_path, "price_trend.png"))
plt.show()

# -------- Stacked Bar Chart --------
stack_data = df.groupby(["bedrooms", "price_category"]).size().unstack(fill_value=0)
stack_data = stack_data.sort_index().head(5)

stack_data.plot(kind='bar', figsize=(10,6))

plt.title("Price Category Distribution by Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(save_path, "price_category_stacked.png"))
plt.show()

# -------- Histogram --------
plt.figure(figsize=(10,5))

upper_limit = df["price"].quantile(0.95)
filtered_prices = df[df["price"] <= upper_limit]["price"]

plt.hist(filtered_prices, bins=30, color="gold")

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.ticklabel_format(style='plain', axis='x')
plt.tight_layout()

plt.savefig(os.path.join(save_path, "price_histogram.png"))
plt.show()

# ==========================================================
# FINAL INSIGHTS
# ==========================================================

print("\n===== FINAL INSIGHTS =====")

luxury = df[df["price_category"] == "Luxury"]
top_bedroom = luxury["bedrooms"].value_counts().idxmax()

print("1. Bedroom category with most luxury houses:", top_bedroom)

common_category = df["price_category"].value_counts().idxmax()
print("2. Most common price category:", common_category)

print("3. Price distribution is right-skewed.")

print("\n ALL TASKS COMPLETED SUCCESSFULLY!")
print(" All graphs saved in:", save_path)