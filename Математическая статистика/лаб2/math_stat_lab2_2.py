import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

alpha = k = 1
theta_real = 5
threshold = 0.1

sample_sizes = np.arange(10, 601, 10)


def posterior_params(data, alpha, k):
    n = len(data)
    alpha_post = alpha + np.sum(data)
    k_post = k + n
    return alpha_post, k_post


results_bayes = []
results_mle = []
for n in sample_sizes:
    estimates_bayes = []
    estimates_mle = []
    diff_counts_bayes = 0
    diff_counts_mle = 0
    for _ in range(100):
        data = poisson.rvs(theta_real, size=n)

        # Bayesian estimate
        alpha_post, k_post = posterior_params(data, alpha, k)
        theta_bayes = alpha_post / k_post

        # MLE estimate
        theta_mle = np.mean(data)

        estimates_bayes.append(theta_bayes)
        estimates_mle.append(theta_mle)

        if abs(theta_bayes - theta_real) > threshold:
            diff_counts_bayes += 1
        if abs(theta_mle - theta_real) > threshold:
            diff_counts_mle += 1

    mean_bayes = np.mean(estimates_bayes)
    std_bayes = np.std(estimates_bayes)
    mean_mle = np.mean(estimates_mle)
    std_mle = np.std(estimates_mle)

    results_bayes.append((n, mean_bayes, std_bayes, diff_counts_bayes))
    results_mle.append((n, mean_mle, std_mle, diff_counts_mle))

results_bayes = np.array(results_bayes)
results_mle = np.array(results_mle)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(results_bayes[:, 0], results_bayes[:, 1], label="Bayesian")
plt.xlabel("Sample Size")
plt.ylabel("Mean Estimate")

plt.subplot(2, 2, 2)
plt.plot(results_bayes[:, 0], results_bayes[:, 2], label="Bayesian")
plt.xlabel("Sample Size")
plt.ylabel("Standard Deviation of Estimate")

plt.subplot(2, 2, 3)
plt.plot(results_bayes[:, 0], results_bayes[:, 3], label="Bayesian")
plt.xlabel("Sample Size")
plt.ylabel("Number of Estimates Exceeding Threshold")

# MLE Plots (overlaid on Bayesian plots)
plt.subplot(2, 2, 1)
plt.plot(results_mle[:, 0], results_mle[:, 1], label="MLE")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(results_mle[:, 0], results_mle[:, 2], label="MLE")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(results_mle[:, 0], results_mle[:, 3], label="MLE")
plt.legend()

plt.suptitle("Comparison of Bayesian and MLE Estimation (Poisson)")
plt.tight_layout()
plt.show()
