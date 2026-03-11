import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# --------------------------
# SIMULATE DATA
# --------------------------
np.random.seed(42)
A = np.random.normal(2.5, 1.5, 30)  # Medicine A
B = np.random.normal(2.0, 0.5, 30)  # Medicine B

# --------------------------
# HYPOTHESIS TESTING (Independent T-Test)
# --------------------------
t_stat, p_val = ttest_ind(A, B)
alpha = 0.05

print("\nHypothesis Testing Results:")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < alpha:
    result = "Null Hypothesis Rejected!\nConclusion: Medicine A and B are different."
else:
    result = "Null Hypothesis Accepted!\nConclusion: No significant difference."

print("\n" + result)

# --------------------------
# BOX PLOT VISUALIZATION
# --------------------------
plt.figure(figsize=(8,5))
plt.boxplot([A, B], labels=["Medicine A", "Medicine B"], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'))
plt.title("Fever Reduction: Medicine A vs B")
plt.ylabel("Fever Reduction (°C)")
plt.grid(True, linestyle="--", alpha=0.5)

# Add result text above the boxplot
plt.text(1.5, max(A.max(), B.max()) + 0.2, result, fontsize=10, color="green",
         ha="center")

plt.show()
