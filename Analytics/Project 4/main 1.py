# ==============================
# SCENARIO 3: CORRECT GRAPH CODE
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import os
print("Current Folder:", os.getcwd())
print("Files:", os.listdir())

# Load dataset
df = pd.read_csv("kc_house_data.csv")

# Clean data
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")

# Convert bedrooms to proper integers
df["bedrooms"] = df["bedrooms"].round().astype(int)

# Filter expensive houses (balanced threshold)
expensive_houses = df[df["price"] > 300000]

print("Total expensive houses:", len(expensive_houses))

# Count number of houses per bedrooms
bedroom_counts = expensive_houses["bedrooms"].value_counts()

# Select top 5 categories
top_bedrooms = bedroom_counts.head(5)

print("\nTop Bedroom Categories:")
print(top_bedrooms)

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(top_bedrooms.index, top_bedrooms.values)

plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Expensive Houses by Bedrooms")

# Rotate labels if needed
plt.xticks(rotation=0)

# Save graph
plt.savefig("expensive_houses_bar_correct.png")

# Show graph
plt.show()