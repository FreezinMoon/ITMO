import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, gamma, expon


# Set seed for reproducibility
np.random.seed(42)

# Parameters
num_samples = 10000
sample_size = 1000
distribution = norm(0, 1)  # Normal distribution as an example

# Initialize arrays to store statistics
sample_means = np.zeros(num_samples)
sample_variances = np.zeros(num_samples)
sample_medians = np.zeros(num_samples)
U1_statistics = np.zeros(num_samples)
U2_statistics = np.zeros(num_samples)

# Generate samples and compute statistics
for i in range(num_samples):
    sample = distribution.rvs(sample_size)
    sample_means[i] = np.mean(sample)
    sample_variances[i] = np.var(sample, ddof=1)  # Unbiased estimator
    sample_medians[i] = np.median(sample)
    order_stat = np.sort(sample)
    U1_statistics[i] = sample_size * distribution.cdf(order_stat[1])
    U2_statistics[i] = sample_size * (1 - distribution.cdf(order_stat[-1]))

# Plotting
fig, axes = plt.subplots(3, 2, figsize=(12, 18))

for ax, data, color, title in zip(axes.flat,
                                  [sample_means, sample_variances, sample_medians, U1_statistics, U2_statistics],
                                  ['g', 'r', 'b', 'c', 'm'],
                                  ['Sample Mean', 'Sample Variance', 'Sample 0.5 Quantile', 'nF(X(2))',
                                   'n(1-F(X(n)))']):
    ax.hist(data, bins=30, density=True, alpha=0.6, color=color, label='Empirical')
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    if title in ['Sample Mean', 'Sample Variance', 'Sample 0.5 Quantile']:
        p = norm.pdf(x, np.mean(data), np.std(data))
    elif title == 'nF(X(2))':
        p = gamma.pdf(x, 2, scale=1)
    else:  # 'n(1-F(X(n)))'
        p = expon.pdf(x, scale=1)
    ax.plot(x, p, 'k--', linewidth=2, label='Theory')
    ax.legend()
    ax.set_title(f'{title}: Mean={np.mean(data):.2f}, SD={np.std(data):.2f}, Median={np.median(data):.2f}', fontsize=10,
                 pad=10)

axes[-1, -1].axis('off')

plt.tight_layout(pad=4.0)
plt.show()
