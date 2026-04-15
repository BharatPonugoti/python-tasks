# Replace Values Using NumPy + Pandas
import pandas as pd
import numpy as np

S = pd.Series([10, 50, 30, 80, 20])

# Replace values > 40 with 0 using NumPy
S_updated = pd.Series(np.where(S > 40, 0, S))

print("Updated Series:\n", S_updated)