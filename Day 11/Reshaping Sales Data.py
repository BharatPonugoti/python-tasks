#Reshaping Sales Data
import numpy as np

# Original data
monthly_sales = np.array([10,20,30,40,50,60,70,80,90,100,110,120])

# Reshape to 4x3
reshaped_sales = monthly_sales.reshape(4, 3)

print(reshaped_sales)