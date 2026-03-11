import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# --------------------------
# OBSERVED DATA (Contingency Table)
# --------------------------
# Rows: Medicine A and Medicine B
# Columns: Recovered, Not Recovered
observed = np.array([[60, 40], 
                     [45, 55]])

# --------------------------
# CHI-SQUARE TEST
# --------------------------
chi2, p_val, dof, expected = chi2_contingency(observed)
alpha = 0.05

print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < alpha:
    result = "Null Hypothesis Rejected!\nConclusion: Medicine's effect is different."
else:
    result = "Null Hypothesis Accepted!\nConclusion: No significant difference."

print("\n" + result)

# --------------------------
# VISUALIZATION (Grouped Bar Plot)
# --------------------------
labels = ["Recovered", "Not Recovered"]
medicine_A = observed[0]
medicine_B = observed[1]

x = np.arange(len(labels))
width = 0.4

plt.figure(figsize=(8,5))
plt.bar(x - width/2, medicine_A, width, label="Medicine A", color="lightblue")
plt.bar(x + width/2, medicine_B, width, label="Medicine B", color="purple")

plt.xticks(x, labels)
plt.ylabel("Number of Patients")
plt.title("Recovery Rates: Medicine A vs B")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Add result text above bars
plt.text(0.5, max(medicine_A.max(), medicine_B.max()) + 3, result, fontsize=10, color="green",
         ha="center")

plt.show()
