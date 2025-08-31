import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# === Шаг 1: Загрузка и предварительная обработка данных ===

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

gender_submission = pd.read_csv('gender_submission.csv')
test_data = test_data.merge(gender_submission, on='PassengerId')

# Обработка пропущенных значений
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())
test_data['Age'] = test_data['Age'].fillna(test_data['Age'].median())

train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])
test_data['Embarked'] = test_data['Embarked'].fillna(test_data['Embarked'].mode()[0])

train_data = train_data.drop('Cabin', axis=1)
test_data = test_data.drop('Cabin', axis=1)

# Кодирование категориальных признаков
train_data['Sex'] = train_data['Sex'].map({'male': 0, 'female': 1})
test_data['Sex'] = test_data['Sex'].map({'male': 0, 'female': 1})

embarked_dummies_train = pd.get_dummies(train_data['Embarked'], prefix='Embarked')
embarked_dummies_test = pd.get_dummies(test_data['Embarked'], prefix='Embarked')

train_data = pd.concat([train_data, embarked_dummies_train], axis=1)
test_data = pd.concat([test_data, embarked_dummies_test], axis=1)

train_data = train_data.drop('Embarked', axis=1)
test_data = test_data.drop('Embarked', axis=1)

# замена отсутствующих столбцов нулями
for col in embarked_dummies_train.columns:
    if col not in test_data.columns:
        test_data[col] = 0

# Нормализация признаков
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_C', 'Embarked_Q', 'Embarked_S']

feature_mean = {}
feature_std = {}

for feature in features:
    mean = train_data[feature].mean()
    std = train_data[feature].std()
    feature_mean[feature] = mean
    feature_std[feature] = std

    train_data[feature] = (train_data[feature] - mean) / std

    if feature in test_data.columns:
        test_data[feature] = (test_data[feature] - mean) / std
    else:
        test_data[feature] = 0

# === Шаг 2: Визуализация статистики по датасету ===

# Получение описательной статистики
stats = train_data[features].describe()

print("\nСтатистика по числовым признакам:")
print(stats)

# Визуализация статистики
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))
axes = axes.flatten()

for idx, feature in enumerate(features):
    sns.histplot(train_data[feature], ax=axes[idx], kde=True)
    axes[idx].set_title(f'Распределение {feature}')
    axes[idx].axvline(train_data[feature].mean(), color='r', linestyle='--', label='Среднее')
    axes[idx].axvline(train_data[feature].median(), color='g', linestyle='-', label='Медиана')
    axes[idx].legend()

plt.tight_layout()
plt.show()

# === Шаг 3: Разделение данных на обучающий и валидационный наборы ===

# Перемешивание данных
train_data = train_data.sample(frac=1, random_state=42).reset_index(drop=True)

X = train_data[features].values
y = train_data['Survived'].values

# Разделение на обучающий и валидационный наборы
split_index = int(len(train_data) * 0.8)
X_train = X[:split_index]
y_train = y[:split_index]

X_val = X[split_index:]
y_val = y[split_index:]


# === Шаг 4: Реализация логистической регрессии ===

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def compute_loss(y_true, y_pred):
    m = y_true.shape[0]
    epsilon = 1e-5  # Чтобы избежать log(0)
    loss = - (1 / m) * np.sum(y_true * np.log(y_pred + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))
    return loss


def gradient_descent(X, y, learning_rate=0.01, num_iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    losses = []

    for i in range(num_iterations):
        z = np.dot(X, theta)
        y_pred = sigmoid(z)

        gradient = (1 / m) * np.dot(X.T, (y_pred - y))
        theta -= learning_rate * gradient

        loss = compute_loss(y, y_pred)
        losses.append(loss)

    return theta, losses


def newton_method(X, y, tolerance=1e-7, max_iterations=100):

    m, n = X.shape
    theta = np.zeros(n)  # Инициализация весов
    prev_theta = np.ones(n) * np.inf  # Для отслеживания изменения весов
    losses = []  # Для записи потерь
    iteration = 0

    while np.linalg.norm(theta - prev_theta, ord=2) > tolerance and iteration < max_iterations:
        prev_theta = theta.copy()
        z = np.dot(X, theta)
        y_pred = sigmoid(z)

        # Вычисление градиента
        gradient = (1 / m) * np.dot(X.T, (y_pred - y))

        # Вычисление гессиана
        S = np.diag(y_pred * (1 - y_pred))
        H = (1 / m) * np.dot(np.dot(X.T, S), X)

        # Инверсия гессиана
        try:
            H_inv = np.linalg.inv(H)
        except np.linalg.LinAlgError:
            H_inv = np.linalg.pinv(H)

        # Обновление весов
        theta -= np.dot(H_inv, gradient)

        # Вычисление функции потерь
        loss = compute_loss(y, y_pred)
        losses.append(loss)

        iteration += 1

    # Проверка на случай отсутствия сходимости
    if iteration >= max_iterations:
        print("Метод Ньютона не сошелся за максимальное число итераций.")

    return theta, losses

def predict(X, theta, threshold=0.5):
    probabilities = sigmoid(np.dot(X, theta))
    return (probabilities >= threshold).astype(int)


# === Шаг 5 и 6: Исследование гиперпараметров и оценка модели ===

learning_rates = [0.001, 0.01, 0.1]
num_iterations_list = [500, 1000, 2000]
methods = ['gradient_descent', 'newton_method']


def evaluate_model(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))

    accuracy = (TP + TN) / len(y_true)
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_score = (2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0)

    return accuracy, precision, recall, f1_score


results = []

# Словари для хранения потерь и метрик
all_losses = {}
all_theta = {}

for method in methods:
    if method == 'gradient_descent':
        for learning_rate in learning_rates:
            for num_iterations in num_iterations_list:
                # Обучение модели
                theta, losses = gradient_descent(X_train, y_train, learning_rate, num_iterations)

                # Сохранение потерь
                key = f"{method}_lr{learning_rate}_iter{num_iterations}"
                all_losses[key] = losses
                all_theta[key] = theta

                # Вычисление метрик на валидационном наборе
                y_val_pred = predict(X_val, theta)
                acc, prec, rec, f1 = evaluate_model(y_val, y_val_pred)

                # Сохранение результатов
                results.append(
                    {'Method': method, 'Learning Rate': learning_rate, 'Iterations': num_iterations, 'Accuracy': acc,
                        'Precision': prec, 'Recall': rec, 'F1-Score': f1, })

    elif method == 'newton_method':
        # Обучение модели
        theta, losses = newton_method(X_train, y_train)
        num_iterations = len(theta)

        # Сохранение потерь
        key = f"{method}_iter{num_iterations}"
        all_losses[key] = losses
        all_theta[key] = theta

        # Вычисление метрик на валидационном наборе
        y_val_pred = predict(X_val, theta)
        acc, prec, rec, f1 = evaluate_model(y_val, y_val_pred)

        # Сохранение результатов
        results.append({'Method': method, 'Learning Rate': None, 'Iterations': num_iterations, 'Accuracy': acc,
            'Precision': prec, 'Recall': rec, 'F1-Score': f1, })

# === Шаг 7: Анализ результатов ===

results_df = pd.DataFrame(results)
print("\nРезультаты экспериментов:")
print(results_df)

best_results = results_df.sort_values(by='F1-Score', ascending=False)
print('\nЛучшие результаты:')
print(best_results.head())

# Визуализация функции потерь для каждой комбинации гиперпараметров
num_plots = len(all_losses)
cols = 3
rows = num_plots // cols + int(num_plots % cols > 0)

fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
axes = axes.flatten()

for idx, (key, losses) in enumerate(all_losses.items()):
    if len(losses) > 1:  # Проверяем, что есть хотя бы две точки
        axes[idx].plot(losses)
        axes[idx].set_title(f"Loss over Iterations\n{key}")
        axes[idx].set_xlabel('Итерация')
        axes[idx].set_ylabel('Loss')
    else:
        axes[idx].text(0.5, 0.5, 'Insufficient Data', ha='center', va='center')
        axes[idx].set_title(f"Loss over Iterations\n{key}")

# Удаление пустых подграфиков
for idx in range(len(all_losses), len(axes)):
    fig.delaxes(axes[idx])

plt.tight_layout()
plt.show()

# Анализ влияния гиперпараметров на производительность модели

# Для градиентного спуска: влияние learning_rate и num_iterations на F1-Score

# gd_results = results_df[results_df['Method'] == 'gradient_descent']
gd_results = results_df
# Построение тепловой карты
pivot_table = gd_results.pivot(index='Learning Rate', columns='Iterations', values='F1-Score')

plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, fmt=".3f", cmap='viridis')
plt.title('F1-Score для гиперпараметров Gradient Descent')
plt.show()

# Выводы о наилучших гиперпараметрах

print("\nАнализ влияния гиперпараметров на производительность модели:")
best_f1_score = best_results.iloc[0]['F1-Score']
best_params = best_results.iloc[0]

print(f"Наилучший F1-Score: {best_f1_score:.4f}")
print("Параметры модели с наилучшим F1-Score:")
print(best_params)


print("\nИзменение F1-Score при варьировании Learning Rate и Iterations:")
print(pivot_table)


# Построение ROC-кривой для лучшей модели

# Функция для вычисления ROC-кривой
def compute_roc_curve(y_true, y_scores):
    thresholds = np.sort(np.unique(y_scores))[::-1]
    tpr_list = []
    fpr_list = []

    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    for threshold in thresholds:
        y_pred = (y_scores >= threshold).astype(int)
        TP = np.sum((y_true == 1) & (y_pred == 1))
        FP = np.sum((y_true == 0) & (y_pred == 1))
        TPR = TP / P if P > 0 else 0  # Recall
        FPR = FP / N if N > 0 else 0

        tpr_list.append(TPR)
        fpr_list.append(FPR)

    return fpr_list, tpr_list


# Функция для вычисления Precision-Recall кривой
def compute_pr_curve(y_true, y_scores):
    thresholds = np.sort(np.unique(y_scores))[::-1]
    precision_list = []
    recall_list = []

    for threshold in thresholds:
        y_pred = (y_scores >= threshold).astype(int)
        TP = np.sum((y_true == 1) & (y_pred == 1))
        FP = np.sum((y_true == 0) & (y_pred == 1))
        FN = np.sum((y_true == 1) & (y_pred == 0))

        precision = TP / (TP + FP) if (TP + FP) > 0 else 1
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0

        precision_list.append(precision)
        recall_list.append(recall)

    return recall_list, precision_list


# Функция для вычисления F1-Score кривой
def compute_f1_curve(y_true, y_scores):
    thresholds = np.sort(np.unique(y_scores))[::-1]
    f1_scores = []

    for threshold in thresholds:
        y_pred = (y_scores >= threshold).astype(int)
        _, precision, recall, f1 = evaluate_model(y_true, y_pred)
        f1_scores.append(f1)

    return thresholds, f1_scores


# Обучение лучшей модели
key_best_model = ''
if best_params['Method'] == 'gradient_descent':
    key_best_model = f"gradient_descent_lr{best_params['Learning Rate']}_iter{int(best_params['Iterations'])}"
elif best_params['Method'] == 'newton_method':
    key_best_model = f"newton_method_iter{int(best_params['Iterations'])}"

theta_best = all_theta[key_best_model]

# Получение вероятностей для валидационного набора
y_val_prob = sigmoid(np.dot(X_val, theta_best))

# Построение ROC-кривой
fpr, tpr = compute_roc_curve(y_val, y_val_prob)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='ROC Curve')
plt.plot([0, 1], [0, 1], 'k--', label='Random Guessing')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid()
plt.show()

# Построение Precision-Recall кривой
recall, precision = compute_pr_curve(y_val, y_val_prob)

plt.figure(figsize=(8, 6))
plt.plot(recall, precision, label='Precision-Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='lower left')
plt.grid()
plt.show()

# Построение F1-Score кривой
thresholds, f1_scores = compute_f1_curve(y_val, y_val_prob)
best_threshold_index = np.argmax(f1_scores)
best_threshold = thresholds[best_threshold_index]

plt.figure(figsize=(8, 6))
plt.plot(thresholds, f1_scores, label='F1-Score Curve')
plt.axvline(best_threshold, color='r', linestyle='--', label=f'Best Threshold = {best_threshold:.4f}')
plt.xlabel('Threshold')
plt.ylabel('F1-Score')
plt.title('F1-Score Curve')
plt.legend(loc='lower left')
plt.grid()
plt.show()

print(f'Лучший порог для F1-Score: {best_threshold:.4f}, Максимальный F1-Score: {f1_scores[best_threshold_index]:.4f}')

# Получение весов лучшей модели
theta_best = all_theta[key_best_model]

# Создание DataFrame для удобства
weights = pd.DataFrame({
    'Feature': features,
    'Weight': theta_best
})

# Сортировка по абсолютному значению веса
weights['Abs_Weight'] = weights['Weight'].abs()
weights_sorted = weights.sort_values(by='Abs_Weight', ascending=False)

print("\nЗначимость признаков в предсказании выживаемости:")
print(weights_sorted[['Feature', 'Weight']])