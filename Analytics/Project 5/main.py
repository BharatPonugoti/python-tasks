'''
=================================================================================================================================
---------------------------------------------📊 Project Title: Cars Data Analysis--------------------------------------
--------------------------------------Analyze Cars Sales dataset using NumPy, Pandas, Matplotlib-----------------------------
=================================================================================================================================
'''
'''
=================================================================================================================================
 📦 1. Import Required Libraries
=================================================================================================================================
 👉 Import numpy
 👉 Import pandas
 👉 Import matplotlib.pyplot
 👉 (Optional) Import os for folder creation
<Import your libraries>
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

'''
=================================================================================================================================
                                     🟢 SCENARIO 1: Data Loading & Basic Cleaning
=================================================================================================================================
�� Tasks:
● Load the dataset using Pandas.
● Display:
○ First 5 rows
○ Last 5 rows
○ Column names
○ Shape of dataset
● Check data types of all columns.
● Check for missing values in:
○ Selling_Price
○ Present_Price
○ Kms_Driven
○ Fuel_Type
● Fill missing values:
○ Selling_Price → mean
○ Present_Price → mean
○ Kms_Driven → mean
○ Fuel_Type → mode
● Convert numeric columns to proper numeric type if required:
○ Selling_Price
○ Present_Price
○ Kms_Driven
○ Year
● Convert Selling_Price and Kms_Driven into NumPy arrays.
● Use NumPy to calculate:
○ minimum selling price
○ maximum selling price
○ average selling price
'''

# ------------------------------
# LOAD DATA
# ------------------------------
df = pd.read_csv("cardata.csv")

# ------------------------------
# BASIC INFO
# ------------------------------
print("FIRST 5 ROWS:\n", df.head())
print("\nLAST 5 ROWS:\n", df.tail())
print("\nCOLUMNS:\n", df.columns)
print("\nSHAPE:\n", df.shape)
print("\nDATA TYPES:\n", df.dtypes)

# ------------------------------
# DATA CLEANING
# ------------------------------
df["Selling_Price"] = pd.to_numeric(df["Selling_Price"], errors="coerce")
df["Present_Price"] = pd.to_numeric(df["Present_Price"], errors="coerce")
df["Kms_Driven"] = pd.to_numeric(df["Kms_Driven"], errors="coerce")
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

df["Selling_Price"] = df["Selling_Price"].fillna(df["Selling_Price"].mean())
df["Present_Price"] = df["Present_Price"].fillna(df["Present_Price"].mean())
df["Kms_Driven"] = df["Kms_Driven"].fillna(df["Kms_Driven"].mean())
df["Fuel_Type"] = df["Fuel_Type"].fillna(df["Fuel_Type"].mode()[0])

# ------------------------------
# NUMPY CALCULATIONS
# ------------------------------
selling_np = df["Selling_Price"].to_numpy()

print("\nMinimum Selling Price:", np.min(selling_np))
print("Maximum Selling Price:", np.max(selling_np))
print("Average Selling Price:", np.mean(selling_np))


'''
=================================================================================================================================
                                     🟢 SCENARIO 2: Selling Price Trend (Line Graph)
=================================================================================================================================
�� Tasks:
● Select:
○ Car_Name
○ Selling_Price
● Take the first 10 rows only using Pandas.
● Convert Selling_Price into a NumPy array.
● Plot a line graph using Matplotlib:
○ X-axis → row index (0–9)
○ Y-axis → Selling Price
● Add:
○ title
○ x-axis label
○ y-axis label
○ markers
● Save the graph with a suitable filename.

'''

# ------------------------------
# SCENARIO 2: LINE GRAPH
# ------------------------------
sample = df[["Car_Name", "Selling_Price"]].head(10)

y = sample["Selling_Price"].to_numpy()

plt.plot(range(len(y)), y, marker='o')
plt.title("Selling Price Trend (First 10 Cars)")
plt.xlabel("Index")
plt.ylabel("Selling Price")

# Save + Show
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/selling_price_line.png")
plt.show()

'''
=================================================================================================================================
                                     🟡 SCENARIO 3: Expensive Cars Analysis (Filtering + Bar)
=================================================================================================================================
�� Tasks:
● Filter cars where:
○ Selling_Price > 10
● Group the filtered data by:
○ Fuel_Type
● Count number of cars in each fuel type.
● Convert:
○ fuel type labels
○ counts
into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Fuel Type
○ Y-axis → Count of expensive cars
● Add:
○ title
○ x-label
○ y-label
● Save the graph.

'''
expensive_cars = df[df['Selling_Price'] > 10]
fuel_counts = expensive_cars.groupby('Fuel_Type').size()
fuel_labels = np.array(fuel_counts.index)
fuel_values = np.array(fuel_counts.values)
plt.bar(fuel_labels, fuel_values, color='skyblue')
plt.title("Fuel Types of Expensive Cars")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/expensive_car_analysis.png")
plt.show()

'''
=================================================================================================================================
                                     🟡 SCENARIO 4: Pie Chart (Fuel Type Distribution) + Save
=================================================================================================================================
�� Tasks:
● Count the number of cars in each:
○ Fuel_Type
● Select all categories or top categories if needed.
● Prepare:
○ labels
○ values
● Convert values into a NumPy array.
● Plot a pie chart using Matplotlib.
● Add:
○ percentage labels
○ title
● Save the graph.

'''
counts = df['Fuel_Type'].value_counts()
labels = counts.index
values = np.array(counts.values)  
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Overall Fuel Type Distribution")
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/fuel_type_distribution.png")
plt.show()

'''
=================================================================================================================================
                                     🔴 SCENARIO 5: Present Price vs Selling Price (Scatter Plot)
=================================================================================================================================
�� Tasks:
● Select:
○ Present_Price
○ Selling_Price
● Remove missing values if any.
● Take a smaller sample (for example first 50 or 100 rows) using Pandas.
● Convert both columns into NumPy arrays.
● Plot a scatter plot using Matplotlib:
○ X-axis → Present_Price
○ Y-axis → Selling_Price
● Add:
○ title
○ x-label
○ y-label
● Observe whether there is a positive relationship.
● Save the graph.
'''
# 1. Select only the columns we need
price_data = df[['Present_Price', 'Selling_Price']]

# 2. Clean up any missing values to avoid errors in plotting
price_data = price_data.dropna()

# 3. Take a smaller sample (first 100 rows) so the plot isn't too crowded
sample_data = price_data.head(100)

# 4. Convert columns into NumPy arrays for processing
x_present = sample_data['Present_Price'].to_numpy()
y_selling = sample_data['Selling_Price'].to_numpy()

# 5. Create the Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(x_present, y_selling, alpha=0.7, edgecolors='k')

# Adding the requested details
plt.title('Relationship: Present Price vs Selling Price')
plt.xlabel('Present Price (Showroom Price)')
plt.ylabel('Selling Price (Resale Price)')
plt.grid(True, linestyle='--', alpha=0.6)

# Save the graph
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/present_vs_selling_scatter.png")
plt.show()


'''
=================================================================================================================================
                                     🟢 SCENARIO 6: Car Age Category Analysis + Bar Chart
=================================================================================================================================
�� Tasks:
● Create a new column using Pandas:
Car Age Category
● Year >= 2015 → "New"
● 2010 to 2014 → "Medium"
● < 2010 → "Old"
● Count number of cars in each:
○ Car Age Category
● Convert category names and counts into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Car Age Category
○ Y-axis → Count
● Add title and labels.
● Save the graph.
'''

# 1. Create a logic function to categorize the cars by year
def categorize_age(year):
    if year >= 2015:
        return "New"
    elif 2010 <= year <= 2014:
        return "Medium"
    else:
        return "Old"

# 2. Create the new column using Pandas
df['Car Age Category'] = df['Year'].apply(categorize_age)

# 3. Count how many cars fall into each category
category_counts = df['Car Age Category'].value_counts()

# 4. Convert names and counts into NumPy arrays
age_labels = category_counts.index.to_numpy()
age_values = category_counts.values

# 5. Create the Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(age_labels, age_values)

# Adding the requested details
plt.title('Car Distribution by Age Category')
plt.xlabel('Car Age Category')
plt.ylabel('Number of Cars')

# Save the graph
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/car_age_category_bar.png")
plt.show()

print("Graphs have been generated and saved successfully.")

'''
=================================================================================================================================
                                     🟢 SCENARIO 7: Kms Driven Distribution (Histogram)
================================================================================================================================
�� Tasks:
● Select:
○ Kms_Driven
● Convert it into a NumPy array.
● Plot a histogram using Matplotlib:
○ X-axis → Kms Driven
○ Y-axis → Frequency
● Choose suitable number of bins.
● Add:
○ title
○ x-label
○ y-label
● Save the graph.
● Observe whether most cars have lower or higher mileage.

'''
# Select Kms_Driven column
kms = df["Kms_Driven"]

# Convert into NumPy array
kms_array = np.array(kms)

# Plot histogram
plt.figure(figsize=(8,5))
plt.hist(kms_array, bins=15)   # you can change bins value if needed

# Add title and labels
plt.title("Kms Driven Distribution")
plt.xlabel("Kms Driven")
plt.ylabel("Frequency")

# Save graph
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/kms_driven_histogram.png")

# Show graph
plt.show()


'''
=================================================================================================================================
                                     🟢 SCENARIO 8: Transmission - Wise Selling Price Comparison
=================================================================================================================================
�� Tasks:
● Group data by:
○ Transmission
● Calculate:
○ average Selling_Price
● Convert transmission labels and average prices into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Transmission
○ Y-axis → Average Selling Price
● Add title and labels.
● Save the graph.

'''
# Group by Transmission and calculate average Selling_Price
avg_price = df.groupby("Transmission")["Selling_Price"].mean()

# Convert into NumPy arrays
transmission_array = np.array(avg_price.index)
price_array = np.array(avg_price.values)

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(transmission_array, price_array)

# Add title and labels
plt.title("Average Selling Price by Transmission")
plt.xlabel("Transmission")
plt.ylabel("Average Selling Price")

# Save graph
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/transmission_selling_price.png")

# Show graph
plt.show()

'''
=================================================================================================================================
                                     🟢 SCENARIO 9: Seller Type Analysis
=================================================================================================================================
�� Tasks:
● Count number of cars by:
○ Seller_Type
● Convert results into NumPy arrays.
● Plot a bar chart or pie chart using Matplotlib.
● Add labels and title.
● Save the graph.
● Identify which seller type is more common.
'''

# ------------------------------
# COUNT SELLER TYPES
# ------------------------------
seller_counts = df["Seller_Type"].value_counts().sort_values(ascending=False)

# Convert to NumPy
seller_labels = seller_counts.index.to_numpy()
seller_values = seller_counts.values

# ------------------------------
# BAR CHART (Clean & Colorful)
# ------------------------------
plt.figure(figsize=(8,5))

plt.bar(seller_labels, seller_values, color=["#4CAF50", "#2196F3", "#FF9800"])

plt.title("Seller Type Distribution", fontsize=14)
plt.xlabel("Seller Type", fontsize=12)
plt.ylabel("Number of Cars", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("C:/Analytics/Project 5/pictorial_analysis/seller_type_bar.png")
plt.show()


# ------------------------------
# PIE CHART
# ------------------------------
plt.figure(figsize=(6,6))

plt.pie(
    seller_values,
    labels=seller_labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=["#FF6F61", "#6B5B95", "#88B04B"],
    textprops={'fontsize': 11}
)

plt.title("Seller Type Distribution (Pie Chart)", fontsize=14)

plt.tight_layout()
plt.savefig("C:/Analytics/Project 5/pictorial_analysis/seller_type_pie.png")
plt.show()


# ------------------------------
# INSIGHT
# ------------------------------
most_common_seller = seller_counts.idxmax()
print("\nMost Common Seller Type:", most_common_seller)

'''
=================================================================================================================================
                                     🟢 SCENARIO 10: Advanced Analysis + Multiple Graphs
=================================================================================================================================
�� Part 1: Feature Creation
Create a new column:
Price Difference
● Price Difference = Present_Price - Selling_Price
This shows how much value the car has depreciated.
�� Part 2: NumPy Usage
● Convert Selling_Price into a NumPy array.
● Use NumPy to calculate price changes between consecutive rows using:
○ np.diff()
● Convert Price Difference column into a NumPy array.
● Find:
○ average depreciation
○ maximum depreciation
○ minimum depreciation
�� Part 3: Visualizations
�� Line Graph
● Plot Selling_Price trend for all cars.
�� Bar Chart
● Show average Selling_Price by Fuel_Type.
�� Histogram
● Plot distribution of Selling_Price.
�� Part 4: Insights
Answer these:
● Which fuel type has the highest average selling price?
● Which transmission type has higher average selling price?
● Are most cars concentrated in lower selling prices or higher selling prices?
● Do older cars tend to have lower selling prices?
'''
'''
=================================================================================================================================
                                     🟢 SCENARIO 10: Advanced Analysis + Multiple Graphs
=================================================================================================================================
'''

# ------------------------------
# PART 1: FEATURE CREATION
# ------------------------------
df["Price_Difference"] = df["Present_Price"] - df["Selling_Price"]

# ------------------------------
# PART 2: NUMPY CALCULATIONS
# ------------------------------
selling_np = df["Selling_Price"].to_numpy()
price_diff_np = df["Price_Difference"].to_numpy()

price_change = np.diff(selling_np)

avg_depreciation = np.mean(price_diff_np)
max_depreciation = np.max(price_diff_np)
min_depreciation = np.min(price_diff_np)

print("\nAverage Depreciation:", avg_depreciation)
print("Maximum Depreciation:", max_depreciation)
print("Minimum Depreciation:", min_depreciation)


# ------------------------------
# PART 3: VISUALIZATIONS
# ------------------------------

# -------- 1. LINE GRAPH (Meaningful Trend) --------
year_avg = df.groupby("Year")["Selling_Price"].mean().sort_index()

plt.figure(figsize=(10,5))

plt.plot(year_avg.index, year_avg.values, marker='o', color="#E91E63")

plt.title("Average Selling Price by Year", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Selling Price", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("C:/Analytics/Project 5/pictorial_analysis/year_trend.png")
plt.show()


# -------- 2. BAR CHART (Fuel Type Insight) --------
fuel_avg = df.groupby("Fuel_Type")["Selling_Price"].mean().sort_values()

plt.figure(figsize=(8,5))

fuel_avg.plot(kind='bar', color="#3F51B5")

plt.title("Average Selling Price by Fuel Type", fontsize=14)
plt.xlabel("Fuel Type", fontsize=12)
plt.ylabel("Average Selling Price", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("C:/Analytics/Project 5/pictorial_analysis/fuel_bar.png")
plt.show()


# -------- 3. BAR CHART (Transmission Insight) --------
trans_avg = df.groupby("Transmission")["Selling_Price"].mean().sort_values()

plt.figure(figsize=(8,5))

trans_avg.plot(kind='bar', color="#009688")

plt.title("Average Selling Price by Transmission", fontsize=14)
plt.xlabel("Transmission", fontsize=12)
plt.ylabel("Average Selling Price", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("C:/Analytics/Project 5/pictorial_analysis/transmission_bar.png")
plt.show()


# -------- 4. HISTOGRAM (Clean Distribution) --------
plt.figure(figsize=(8,5))

plt.hist(selling_np, bins=20, color="#FF5722", edgecolor='black')

plt.title("Selling Price Distribution", fontsize=14)
plt.xlabel("Selling Price", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("C:/Analytics/Project 5/pictorial_analysis/selling_hist.png")
plt.show()


# ------------------------------
# PART 4: INSIGHTS
# ------------------------------
highest_fuel = fuel_avg.idxmax()
highest_trans = trans_avg.idxmax()

median_price = np.median(selling_np)

df["Car_Age"] = 2025 - df["Year"]
corr = df["Car_Age"].corr(df["Selling_Price"])

print("\nINSIGHTS:")
print("Fuel Type with Highest Avg Selling Price:", highest_fuel)
print("Transmission with Highest Avg Selling Price:", highest_trans)

if median_price < np.mean(selling_np):
    print("Most cars are concentrated in lower price range.")
else:
    print("Most cars are concentrated in higher price range.")

if corr < 0:
    print("Older cars tend to have lower selling prices.")
else:
    print("No strong negative relation between age and price.")
'''
================================================================================================================
-----------------------------------------------------THE END----------------------------------------------------
================================================================================================================
'''

