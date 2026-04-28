# ==============================
# SCENARIO 3: FILTERING + BAR CHART + SAVE
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset (make sure file is in same folder)
df = pd.read_csv(r"C:\Analytics\Project 5\kc_house_data.csv")

# 1. Filter houses where price > 1,000,000
expensive_houses = df[df["price"] > 1000000]

print("Total expensive houses:", len(expensive_houses))

# 2. Count number of houses per bedrooms
bedroom_counts = expensive_houses["bedrooms"].value_counts()

# 3. Select top bedroom categories (top 5)
top_bedrooms = bedroom_counts.head(5)

print("\nTop Bedroom Categories:")
print(top_bedrooms)

# 4. Convert results to NumPy arrays
bedrooms = top_bedrooms.index.to_numpy()
counts = top_bedrooms.values

# 5. Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(bedrooms, counts)

plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Expensive Houses by Bedrooms")

# 6. Rotate labels
plt.xticks(rotation=45)

# 7. Save graph
plt.savefig("expensive_houses_bar.png")

# Show graph
plt.show()