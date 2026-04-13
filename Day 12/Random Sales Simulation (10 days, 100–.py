# Random Sales Simulation (10 days, 100–500)
import numpy as np

sales = np.random.randint(100, 501, 10)

print("Sales:", sales)
print("Average Sales:", np.mean(sales))