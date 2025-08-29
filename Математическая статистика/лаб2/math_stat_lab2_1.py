import matplotlib.pyplot as plt
import numpy as np


def estimate_theta_squared(sample_sizes, theta_real, num_samples, threshold):
    """
    Estimate theta squared for the Laplace distribution using the method of moments.
    """
    estimates = {n: [] for n in sample_sizes}
    deviations = {n: [] for n in sample_sizes}
    exceed_counts = {n: 0 for n in sample_sizes}

    np.random.seed(42)  # Ensuring reproducibility
    for n in sample_sizes:
        for _ in range(num_samples):
            sample = np.random.laplace(loc=0, scale=theta_real, size=n)
            estimate = np.var(sample, ddof=1) / 2
            estimates[n].append(estimate)
            deviation = abs(estimate - theta_real ** 2)
            deviations[n].append(deviation)
            if deviation > threshold:
                exceed_counts[n] += 1

    # Calculating sample characteristics
    mean_estimates = {n: np.mean(estimates[n]) for n in sample_sizes}
    var_estimates = {n: np.var(estimates[n], ddof=1) for n in sample_sizes}
    mse_estimates = {n: np.mean([d ** 2 for d in deviations[n]]) for n in sample_sizes}

    return estimates, mean_estimates, var_estimates, mse_estimates, exceed_counts


def plot_results(sample_sizes, estimates, mean_estimates, var_estimates, mse_estimates, exceed_counts, theta_real):
    """
    Plot all results of the estimation process: estimates, mean, variance, MSE, and exceedance counts.
    """
    # Plotting the estimates for each sample size
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    for n in sample_sizes:
        plt.scatter([n] * len(estimates[n]), estimates[n], alpha=0.5)
    plt.plot(sample_sizes, [theta_real ** 2] * len(sample_sizes), 'r--', label='Real θ²')
    plt.xlabel('Sample Size')
    plt.ylabel('Estimate of θ²')
    plt.title('Estimates by Sample Size')
    plt.legend()
    plt.grid(True)

    # Mean Estimates
    plt.subplot(2, 3, 2)
    plt.plot(sample_sizes, list(mean_estimates.values()), marker='o')
    plt.axhline(y=theta_real ** 2, color='r', linestyle='--')
    plt.xlabel('Sample Size')
    plt.ylabel('Mean Estimate of θ²')
    plt.title('Mean Estimates')
    plt.grid(True)

    # Variance of Estimates
    plt.subplot(2, 3, 3)
    plt.plot(sample_sizes, list(var_estimates.values()), marker='o')
    plt.xlabel('Sample Size')
    plt.ylabel('Variance of Estimates')
    plt.title('Variance of Estimates')
    plt.grid(True)

    # MSE of Estimates
    plt.subplot(2, 3, 4)
    plt.plot(sample_sizes, list(mse_estimates.values()), marker='o')
    plt.xlabel('Sample Size')
    plt.ylabel('MSE of Estimates')
    plt.title('MSE of Estimates')
    plt.grid(True)

    # Exceedance Counts
    plt.subplot(2, 3, 5)
    plt.bar(sample_sizes, list(exceed_counts.values()))
    plt.xlabel('Sample Size')
    plt.ylabel('Count of Exceedance')
    plt.title('Exceedance Counts')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# Parameters
sample_sizes = [10, 30, 50, 100, 200, 500, 1000]
theta_real = 0.5
num_samples = 1000
threshold = 0.1

# Run the experiment
estimates, mean_estimates, var_estimates, mse_estimates, exceed_counts = estimate_theta_squared(sample_sizes,
                                                                                                theta_real, num_samples,
                                                                                                threshold)
# Display results
print("Mean Estimates:", mean_estimates)
print("Variance of Estimates:", var_estimates)
print("MSE of Estimates:", mse_estimates)
print("Counts exceeding threshold:", exceed_counts)
plot_results(sample_sizes, estimates, mean_estimates, var_estimates, mse_estimates, exceed_counts, theta_real)
