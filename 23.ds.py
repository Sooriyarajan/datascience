import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
np.random.seed(0)  # for reproducibility
control_group_data = np.random.normal(30, 5, 50)  # Placeholder data
treatment_group_data = np.random.normal(35, 5, 50)  # Placeholder data
t_statistic, p_value = stats.ttest_ind(control_group_data, treatment_group_data)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("The new treatment has a statistically significant effect.")
else:
    print("There is no statistically significant effect observed.")
