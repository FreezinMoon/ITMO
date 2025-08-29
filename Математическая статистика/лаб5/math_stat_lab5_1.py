import numpy as np
import pandas as pd
from scipy import stats

file_path = './mobile_phones.csv'
data = pd.read_csv(file_path)

X = data[['sc_h', 'sc_w', 'battery_power']]
y = data['mobile_wt']

# Добавляем свободный коэффициент
X = np.column_stack((np.ones(len(X)), X))

# Построение модели методом наименьших квадратов
X_transpose = X.T
X_transpose_dot_X = X_transpose.dot(X)
inv_X_transpose_dot_X = np.linalg.inv(X_transpose_dot_X)
X_transpose_dot_y = X_transpose.dot(y)
beta_hat = inv_X_transpose_dot_X.dot(X_transpose_dot_y)

# Предсказанные значения и остатки
y_hat = X.dot(beta_hat)
residuals = y - y_hat

# Остаточная дисперсия
rss = np.sum(residuals ** 2)
n = len(y)
k = X.shape[1]
residual_var = rss / (n - k)

# Стандартные ошибки коэффициентов
var_beta_hat = np.diag(inv_X_transpose_dot_X) * residual_var
se_beta_hat = np.sqrt(var_beta_hat)

# Доверительные интервалы для коэффициентов
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha / 2, df=n - k)
conf_intervals = np.column_stack((beta_hat - t_critical * se_beta_hat, beta_hat + t_critical * se_beta_hat))

# Коэффициент детерминации
tss = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (rss / tss)

# Проверка гипотез
# 1. Чем больше высота экрана, тем больше масса
t_stat_sc_h = beta_hat[1] / se_beta_hat[1]
p_value_sc_h = 2 * (1 - stats.t.cdf(np.abs(t_stat_sc_h), df=n - k))

# 2. Чем больше ширина экрана, тем больше масса
t_stat_sc_w = beta_hat[2] / se_beta_hat[2]
p_value_sc_w = 2 * (1 - stats.t.cdf(np.abs(t_stat_sc_w), df=n - k))

# 3. Гипотеза H0: коэффициенты при sc_w и battery_power равны нулю
R = np.array([[0, 1, 0, 0], [0, 0, 1, 0]])
q = np.array([0, 0])
restriction = R.dot(beta_hat) - q
F_statistic = (restriction.T.dot(np.linalg.inv(R.dot(inv_X_transpose_dot_X).dot(R.T))).dot(restriction) / R.shape[
    0]) / residual_var
p_value_F_test = 1 - stats.f.cdf(F_statistic, R.shape[0], n - k)

# Сравнение с готовой реализацией
import statsmodels.api as sm

X_sm = sm.add_constant(data[['sc_h', 'sc_w', 'battery_power']])
model_sm = sm.OLS(y, X_sm).fit()

# Вывод результатов
print("Результаты ручного вычисления:\n")
print(f"Коэффициенты: {beta_hat}")
print(f"Стандартные ошибки: {se_beta_hat}")
print(f"Доверительные интервалы: {conf_intervals}")
print(f"Остаточная дисперсия: {residual_var}")
print(f"Коэффициент детерминации (R^2): {r_squared}")
print("\nПроверка гипотез:")
print(f"1. Чем больше высота экрана, тем больше масса: t-статистика = {t_stat_sc_h}, p-значение = {p_value_sc_h}")
print(f"2. Чем больше ширина экрана, тем больше масса: t-статистика = {t_stat_sc_w}, p-значение = {p_value_sc_w}")
print(
    f"3. Гипотеза H0: коэффициенты при sc_w и battery_power равны нулю: F-статистика = {F_statistic}, p-значение = {p_value_F_test}")

print("\nРезультаты готовой реализации (statsmodels):\n")
print(model_sm.summary())