import numpy as np
from scipy import stats


def laplace_confidence_intervals(n, mu, b, num_simulations=1000, confidence_level=0.95):
    sigma = np.sqrt(2) * b
    standard_error = sigma / np.sqrt(n)
    z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)

    lower_bounds = []
    upper_bounds = []
    for _ in range(num_simulations):
        sample = np.random.laplace(mu, b, n)
        sample_mean = np.mean(sample)
        lower_bound = sample_mean - z_score * standard_error
        upper_bound = sample_mean + z_score * standard_error
        lower_bounds.append(lower_bound)
        upper_bounds.append(upper_bound)

    return np.mean(lower_bounds), np.mean(upper_bounds)


# Parameters for the Laplace distribution
mu = 2
b = 1
n1 = 25
n2 = 10000
num_simulations = 1000
confidence_level = 0.95

lower_bound_25, upper_bound_25 = laplace_confidence_intervals(n1, mu, b, num_simulations, confidence_level)
lower_bound_10000, upper_bound_10000 = laplace_confidence_intervals(n2, mu, b, num_simulations, confidence_level)

print(f"Asymptotic 95% confidence interval for mu with sample size {n1}: [{lower_bound_25:.2f}, {upper_bound_25:.2f}]")
print(
    f"Asymptotic 95% confidence interval for mu with sample size {n2}: [{lower_bound_10000:.2f}, {upper_bound_10000:.2f}]")
