import pandas as pd
from scipy import stats

# Загрузка данных
df = pd.read_csv('exams_dataset.csv')

# 1. Проверка гипотезы о неразличимости количества сдающих мужчин и женщин
# Формализация гипотез:
# H0: Количество сдающих мужчин и женщин неразличимо (популяции равны).
# H1: Количество сдающих мужчин и женщин различимо (популяции не равны).

# Подсчет количества мужчин и женщин
gender_counts = df['gender'].value_counts()
print("Gender counts:\n", gender_counts)

# Тест хи-квадрат
chi2_gender, p_gender = stats.chisquare(gender_counts)
print(f"Chi-square test for gender: chi2 = {chi2_gender}, p-value = {p_gender}")

# Проверка гипотезы о неразличимости этнической принадлежности
# Формализация гипотез:
# H0: Распределение этнической принадлежности одинаково.
# H1: Распределение этнической принадлежности различимо.

# Подсчет этнической принадлежности
ethnicity_counts = df['race/ethnicity'].value_counts()
print("Ethnicity counts:\n", ethnicity_counts)

# Тест хи-квадрат
chi2_ethnicity, p_ethnicity = stats.chisquare(ethnicity_counts)
print(f"Chi-square test for ethnicity: chi2 = {chi2_ethnicity}, p-value = {p_ethnicity}")

# 2. Проверка гипотезы об однородности результатов по математике и письменной части
# Формализация гипотез:
# H0: Средние оценки по математике и письменной части одинаковы.
# H1: Средние оценки по математике и письменной части различны.

math_scores = df['math score']
writing_scores = df['writing score']

# Тест t-Стьюдента для связанных выборок
t_test_scores, p_scores = stats.ttest_rel(math_scores, writing_scores)
print(f"T-test for scores: t-statistic = {t_test_scores}, p-value = {p_scores}")

# Вилкоксонов тест
wilcoxon_test_scores, p_wilcoxon_scores = stats.wilcoxon(math_scores, writing_scores)
print(f"Wilcoxon test for scores: statistic = {wilcoxon_test_scores}, p-value = {p_wilcoxon_scores}")

# 3. Проверка гипотезы о влиянии подготовительных курсов на результаты экзаменов
# Формализация гипотез:
# H0: Средние баллы для студентов, прошедших и не прошедших подготовительные курсы, одинаковы.
# H1: Средние баллы для студентов, прошедших и не прошедших подготовительные курсы, различны.

# Вычисление итогового балла
df['total score'] = df['math score'] + df['reading score'] + df['writing score']

# Разделение данных
prep_course_yes = df[df['test preparation course'] == 'completed']['total score']
prep_course_no = df[df['test preparation course'] == 'none']['total score']

# Тест t-Стьюдента для независимых выборок
t_test_course, p_course = stats.ttest_ind(prep_course_yes, prep_course_no)
print(f"T-test for preparation course: t-statistic = {t_test_course}, p-value = {p_course}")

# U-критерий Манна-Уитни
u, p_mannwhitney_course = stats.mannwhitneyu(prep_course_yes, prep_course_no, alternative='two-sided')
print(f"Mann-Whitney test for preparation course: U = {u}, p-value = {p_mannwhitney_course}")
