import pandas as pd
from scipy.stats import f

file_path = 'exams_dataset.csv'
data = pd.read_csv(file_path)

# Вычисление суммарного балла за все три экзамена
data['total_score'] = data['math score'] + data['reading score'] + data['writing score']

# Разделение данных по уровням фактора (этнической/национальной группы)
groups = data.groupby('race/ethnicity')['total_score']

# Общее количество наблюдений
n = len(data)

# Общее количество групп
k = groups.ngroups

# Вычисление общей средней
grand_mean = data['total_score'].mean()

# Вычисление межгрупповой суммы квадратов (SSB)
SSB = sum(groups.size() * (groups.mean() - grand_mean) ** 2)

# Вычисление внутригрупповой суммы квадратов (SSW)
SSW = sum(((group - group.mean()) ** 2).sum() for name, group in groups)

# Вычисление межгрупповой и внутригрупповой дисперсий
MSB = SSB / (k - 1)
MSW = SSW / (n - k)

# Вычисление F-статистики
F_statistic = MSB / MSW

# Вычисление p-значения
p_value = 1 - f.cdf(F_statistic, k - 1, n - k)

# Вывод результатов
print("Результаты однофакторного дисперсионного анализа (ANOVA):")
print(f"Межгрупповая сумма квадратов (SSB): {SSB}")
print(f"Внутригрупповая сумма квадратов (SSW): {SSW}")
print(f"Межгрупповая дисперсия (MSB): {MSB}")
print(f"Внутригрупповая дисперсия (MSW): {MSW}")
print(f"F-статистика: {F_statistic}")
print(f"p-значение: {p_value}")

# Сравнение с готовой реализацией
import statsmodels.stats.multicomp as multi

mc = multi.MultiComparison(data['total_score'], data['race/ethnicity'])
tukey_result = mc.tukeyhsd()
print(tukey_result)
