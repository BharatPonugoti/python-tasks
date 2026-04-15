# Missing City Data (NaN Handling)
import pandas as pd

cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}

# Create Series with required index
series = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

print("City Data:")
print(series)

# Identify missing values
missing = series[series.isna()]
print("\nCities with Missing Data:")
print(missing)