import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
df = pd.read_csv('mobile_phones.csv')

# 1. Analysis of model characteristics
num_dual_sim = df['dual_sim'].sum()
num_3g_supported = df['three_g'].sum()
max_cpu_cores = df['n_cores'].max()

print(f"Models supporting 2 SIM cards: {num_dual_sim}")
print(f"Models supporting 3G: {num_3g_supported}")
print(f"Highest number of CPU cores: {max_cpu_cores}")

# 2. Selective statistics for battery capacity
mean_battery = df['battery_power'].mean()
var_battery = df['battery_power'].var(ddof=1)
median_battery = df['battery_power'].median()
quantile_battery = df['battery_power'].quantile(0.4)

print(f"Average battery capacity: {mean_battery}")
print(f"Variance of battery capacity: {var_battery}")
print(f"Median of battery capacity: {median_battery}")
print(f"2/5th quantile of battery capacity: {quantile_battery}")

# 3. Visualization
plt.figure(figsize=(15, 5))

# Histogram
plt.subplot(1, 3, 1)
sns.histplot(df['battery_power'], kde=True)
plt.title('Histogram of Battery Capacity')

# Box-plot of the entire population
plt.subplot(1, 3, 2)
sns.boxplot(y=df['battery_power'])
plt.title('Box-plot of Battery Capacity')

# Box-plot by Wi-Fi support
plt.subplot(1, 3, 3)
sns.boxplot(x='wifi', y='battery_power', data=df)
plt.title('Box-plot of Battery Capacity by Wi-Fi')

plt.tight_layout()
plt.show()

# Empirical distribution function
plt.figure(figsize=(7, 5))
sns.ecdfplot(df['battery_power'])
plt.title('Empirical Distribution Function of Battery Capacity')
plt.show()
