import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# SCENARIO 1: LOAD + CLEAN
# ------------------------------
df = pd.read_csv("scottish_hills.csv")

# Convert Height
df["Height"] = pd.to_numeric(df["Height"], errors='coerce')

# Fill missing values
df["Height"].fillna(df["Height"].mean(), inplace=True)

# Create Region
lat_mid = df["Latitude"].median()
lon_mid = df["Longitude"].median()

def assign_region(row):
    if row["Latitude"] >= lat_mid and row["Longitude"] >= lon_mid:
        return "North-East"
    elif row["Latitude"] >= lat_mid:
        return "North-West"
    elif row["Longitude"] >= lon_mid:
        return "South-East"
    else:
        return "South-West"

df["Region"] = df.apply(assign_region, axis=1)

# ------------------------------
# SCENARIO 2: LINE GRAPH
# ------------------------------
subset = df[["Hill Name", "Height"]].head(10)
heights_10 = np.array(subset["Height"])

plt.figure()
plt.plot(range(10), heights_10, marker='o')
plt.title("Height Trend of First 10 Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.savefig("hill_heights_line.png")
plt.show()

# ------------------------------
# SCENARIO 3: BAR CHART
# ------------------------------
tall_hills = df[df["Height"] > 900]
region_counts = tall_hills["Region"].value_counts()

plt.figure()
plt.bar(region_counts.index, region_counts.values)
plt.title("Tall Hills (>900m) per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.savefig("tall_hills_bar.png")
plt.show()

# ------------------------------
# SCENARIO 4: PIE CHART
# ------------------------------
region_dist = df["Region"].value_counts().head(5)

plt.figure()
plt.pie(region_dist, labels=region_dist.index, autopct="%1.1f%%")
plt.title("Region Distribution of Hills")
plt.savefig("region_distribution.png")
plt.show()

# ------------------------------
# SCENARIO 5: ADVANCED ANALYSIS
# ------------------------------

# Height Category
def height_category(h):
    if h >= 1000:
        return "Very High"
    elif h >= 800:
        return "High"
    else:
        return "Moderate"

df["Height Category"] = df["Height"].apply(height_category)

# NumPy diff
heights_all = np.array(df["Height"])
print("Height Differences (first 10):")
print(np.diff(heights_all)[:10])

# Line Graph
plt.figure()
plt.plot(heights_all)
plt.title("Height Trend of All Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.savefig("height_trend.png")
plt.show()

# Stacked Bar Chart
category_counts = df.groupby(["Region", "Height Category"]).size().unstack(fill_value=0)
category_counts.plot(kind="bar", stacked=True)
plt.title("Height Category per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.savefig("height_category_stacked.png")
plt.show()

# Histogram
plt.figure()
plt.hist(heights_all, bins=10)
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.savefig("height_histogram.png")
plt.show()