import numpy as np
import scipy.stats as stats

def compute_t_confidence_intervals(n, m, mu1, mu2, sigma1, sigma2, num_simulations=1000, confidence_level=0.95):
    tau = mu1 - mu2  # Истинная разность средних
    alpha = 1 - confidence_level

    coverage_count_25 = 0
    coverage_count_10000 = 0

    for _ in range(num_simulations):
        # Генерация выборок для n = 25
        X_25 = np.random.normal(mu1, sigma1, n)
        Y_25 = np.random.normal(mu2, sigma2, m)
        diff_25 = X_25.mean() - Y_25.mean()
        s1_sq_25 = np.var(X_25, ddof=1)
        s2_sq_25 = np.var(Y_25, ddof=1)
        se_25 = np.sqrt(s1_sq_25/n + s2_sq_25/m)
        # Расчет степеней свободы по формуле Саттерауэйта
        df_25 = (s1_sq_25/n + s2_sq_25/m)**2 / ((s1_sq_25**2)/(n**2*(n-1)) + (s2_sq_25**2)/(m**2*(m-1)))
        t_crit_25 = stats.t.ppf(1 - alpha/2, df_25)
        ci_25 = (diff_25 - t_crit_25 * se_25, diff_25 + t_crit_25 * se_25)
        if ci_25[0] <= tau <= ci_25[1]:
            coverage_count_25 += 1

        # Генерация выборок для n = 10000
        X_10000 = np.random.normal(mu1, sigma1, 10000)
        Y_10000 = np.random.normal(mu2, sigma2, 10000)
        diff_10000 = X_10000.mean() - Y_10000.mean()
        s1_sq_10000 = np.var(X_10000, ddof=1)
        s2_sq_10000 = np.var(Y_10000, ddof=1)
        se_10000 = np.sqrt(s1_sq_10000/10000 + s2_sq_10000/10000)
        # Расчет степеней свободы по формуле Саттерауэйта
        df_10000 = (s1_sq_10000/10000 + s2_sq_10000/10000)**2 / ((s1_sq_10000**2)/(10000**2*(10000-1)) + (s2_sq_10000**2)/(10000**2*(10000-1)))
        t_crit_10000 = stats.t.ppf(1 - alpha/2, df_10000)
        ci_10000 = (diff_10000 - t_crit_10000 * se_10000, diff_10000 + t_crit_10000 * se_10000)
        if ci_10000[0] <= tau <= ci_10000[1]:
            coverage_count_10000 += 1

    coverage_rate_25 = coverage_count_25 / num_simulations
    coverage_rate_10000 = coverage_count_10000 / num_simulations

    return coverage_rate_25, coverage_rate_10000

# Параметры
mu1 = 2
mu2 = 1
sigma1 = 1
sigma2 = np.sqrt(0.5)
n = 25
m = 25
num_simulations = 1000
confidence_level = 0.95

coverage_rate_25, coverage_rate_10000 = compute_t_confidence_intervals(n, m, mu1, mu2, sigma1, sigma2, num_simulations, confidence_level)

print(f"Вероятность покрытия для размера выборки {n}: {coverage_rate_25:.4f}")
print(f"Вероятность покрытия для размера выборки {10000}: {coverage_rate_10000:.4f}")
