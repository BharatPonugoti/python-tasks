import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Load dataset
file_path = r"C:\Users\Windows\Downloads\railway_gauges (1).csv"
df = pd.read_csv(file_path)

# 🔹 Clean column names
df.columns = df.columns.str.strip().str.title()

# 🔹 Display first 5 rows (df.head)
print("First 5 rows:\n", df.head())

# 🔹 Using iloc (integer-based indexing)
print("\nUsing iloc (4th row):")
print(df.iloc[3])

# 🔹 Using loc (label-based indexing)
print("\nUsing loc (Broad Gauge column):")
print(df.loc[:, 'Broad Gauge'])

# 🔹 Set 'Year' as index
df.set_index('Year', inplace=True)

# 🔹 Using idxmax()
max_year = df['Broad Gauge'].idxmax()
print("\nYear with maximum Broad Gauge:", max_year)

# 🔹 Plot graph using Pandas
df[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].plot(
    kind='bar',
    figsize=(16,6)
)

# 🔹 Labels and title
plt.xlabel("Year")
plt.ylabel("Total")
plt.title("Gauges: Number of railway tracks installed per year")

# 🔹 Rotate x-axis labels
plt.xticks(rotation=90)

# 🔹 Grid for better look
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 🔹 Adjust layout
plt.tight_layout()

# 🔹 Show graph
plt.show()