# Temperature Monitoring System
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

plt.figure()
plt.plot(df["Day"], df["Temperature"], marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()

plt.figure()
plt.plot(df["Day"], df["Temperature"], marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()

plt.figure()
plt.bar(df["Day"], df["Temperature"])
plt.title("Day-wise Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.show()

high = (df["Temperature"] > 30).sum()
low = (df["Temperature"] <= 30).sum()

plt.figure()
plt.pie([high, low], labels=["High (>30)", "Low (≤30)"], autopct='%1.1f%%')
plt.title("High vs Low Temperature Distribution")
plt.show()

plt.figure()
plt.hist(df["Temperature"], bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(range(len(df)), df["Temperature"])
plt.title("Day Index vs Temperature")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.show()