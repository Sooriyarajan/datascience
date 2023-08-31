import scipy.stats as stats
import pandas as pd
data = pd.read_csv("C:/Users/SOORIYA RAJAN.B/Downloads/customer_data (1).csv")
sample_mean = data['rating'].mean()
standard_error = data['rating'].std() / (len(data) ** 0.5)
confidence_level = 0.95
degrees_of_freedom = len(data) - 1
critical_value = stats.t.ppf((1 + confidence_level) / 2, df=degrees_of_freedom)
lower_bound = sample_mean - (critical_value * standard_error)
upper_bound = sample_mean + (critical_value * standard_error)
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
