# Find Maximum Value
import pandas as pd
import numpy as numpy
import numpy as np
import pandas as pd

arr = np.array([12, 45, 22, 67, 34])

# Convert to Series
s = pd.Series(arr)

# Find maximum value
max_value = s.max()

print("Series:\n", s)
print("Maximum value:", max_value)