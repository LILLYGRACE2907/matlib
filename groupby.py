import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance"],
    "Salary": [40000, 30000, 50000, 45000]
})

summary = df.groupby("Department")["Salary"].mean()

plt.bar(summary.index, summary.values)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()