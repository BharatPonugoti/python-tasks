#Filter High Temperature Values
import numpy as np

# Temperature data
temps = np.array([28, 31, 35, 27, 40, 22])

# Filter values greater than 30
high_temps = temps[temps > 30]

print("Temperatures above 30°C:", high_temps)