# Sales Threshold Filtering
import numpy as np

sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

avg_sales = np.mean(sales)
filtered = sales[sales > avg_sales]

print("Average:", avg_sales)
print("Filtered:", filtered)