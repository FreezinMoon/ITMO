import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('WineDataset.csv')

print("\nКоличество пропущенных значений:")
print(df.isnull().sum().sum())

# Все признаки являются числовыми, включая целевую переменную 'Wine'
print("\nТипы данных в датасете:")
print(df.dtypes)

# Так как отсутствующих значений нет, пропускаем шаг заполнения пропущенных значений

X = df.drop('Wine', axis=1)
y = df['Wine']

X_scaled = (X - X.mean()) / X.std()

print("\nСтатистика стандартизированных признаков:")
with pd.option_context('display.max_columns', 8):
    print(X_scaled.describe().T)

stats = df.describe().T
print("\nОписательная статистика признаков:")
with pd.option_context('display.max_columns', 8):
    print(stats)

X.hist(bins=15, figsize=(15, 10), layout=(4, 4))
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 10))
for i, column in enumerate(X.columns, 1):
    plt.subplot(4, 4, i)
    sns.boxplot(y=X[column])
    plt.title(column)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.xticks(rotation=45)
plt.title('Матрица корреляций')
plt.show()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_feature = 'Alcohol'
y_feature = 'Malic Acid'
z_feature = 'Color intensity'

ax.scatter(df[x_feature], df[y_feature], df[z_feature], c=df['Wine'], cmap='viridis', s=60)
ax.set_xlabel(x_feature)
ax.set_ylabel(y_feature)
ax.set_zlabel(z_feature)
plt.title('3D-визуализация признаков')
plt.show()


def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


def k_nearest_neighbors(X_train, y_train, X_test_instance, k):
    distances = []
    for i in range(len(X_train)):
        distance = euclidean_distance(X_train[i], X_test_instance)
        distances.append((distance, y_train[i]))

    distances.sort(key=lambda x: x[0])

    neighbors = distances[:k]

    classes = [neighbor[1] for neighbor in neighbors]

    prediction = max(set(classes), key=classes.count)
    return prediction


X_scaled['Wine'] = y.values

df_shuffled = X_scaled.sample(frac=1, random_state=42).reset_index(drop=True)

train_size = int(0.8 * len(df_shuffled))
train_data = df_shuffled.iloc[:train_size]
test_data = df_shuffled.iloc[train_size:]

X_train = train_data.drop('Wine', axis=1).values
y_train = train_data['Wine'].values

X_test = test_data.drop('Wine', axis=1).values
y_test = test_data['Wine'].values

# Модель 1: случайный выбор 5 признаков
np.random.seed(42)
random_features_indices = np.random.choice(X_train.shape[1], size=5, replace=False)
random_features = [X.columns[i] for i in random_features_indices]
print("\nМодель 1: Случайно выбранные признаки:", random_features)

X_train_model1 = X_train[:, random_features_indices]
X_test_model1 = X_test[:, random_features_indices]

# Модель 2: заранее выбранные признаки
fixed_features = ['Alcohol', 'Malic Acid', 'Color intensity']
feature_indices = [X.columns.get_loc(feature) for feature in fixed_features]
print("\nМодель 2: Выбранные признаки:", fixed_features)

X_train_model2 = X_train[:, feature_indices]
X_test_model2 = X_test[:, feature_indices]


# Функция для оценки модели
def evaluate_knn(X_train, y_train, X_test, y_test, k):
    predictions = []
    for i in range(len(X_test)):
        pred = k_nearest_neighbors(X_train, y_train, X_test[i], k)
        predictions.append(pred)

    confusion_matrix = pd.crosstab(pd.Series(y_test, name='Actual'), pd.Series(predictions, name='Predicted'))

    accuracy = np.sum(y_test == predictions) / len(y_test)
    return confusion_matrix, accuracy


k_values = [1, 3, 5, 10, 50]
for k in k_values:
    print(f"\nМодель 1: Оценка при k={k}")
    cm, accuracy = evaluate_knn(X_train_model1, y_train, X_test_model1, y_test, k)
    print("Матрица ошибок:")
    print(cm)
    print(f"Точность: {accuracy:.4f}")

for k in k_values:
    print(f"\nМодель 2: Оценка при k={k}")
    cm, accuracy = evaluate_knn(X_train_model2, y_train, X_test_model2, y_test, k)
    print("Матрица ошибок:")
    print(cm)
    print(f"Точность: {accuracy:.4f}")
