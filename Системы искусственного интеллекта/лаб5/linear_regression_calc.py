import numpy as np
import pandas as pd

df = pd.read_csv('california_housing_train.csv')

df.columns = ['Longitude', 'Latitude', 'HousingMedianAge', 'TotalRooms', 'TotalBedrooms', 'Population', 'Households',
              'MedianIncome', 'MedianHouseValue']

print(df.isnull().sum())

# Обработка отсутствующих значений
df['TotalBedrooms'] = df['TotalBedrooms'].fillna(df['TotalBedrooms'].median())

# Нормировка признаков
X = df.drop('MedianHouseValue', axis=1)
y = df['MedianHouseValue']

X_norm = (X - X.mean()) / X.std()


def train_test_split(X_norm, y, test_size=0.2, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)

    indices = np.arange(X_norm.shape[0])
    np.random.shuffle(indices)

    test_set_size = int(len(indices) * test_size)
    test_indices = indices[:test_set_size]
    train_indices = indices[test_set_size:]

    X_train, X_test = X_norm.iloc[train_indices], X_norm.iloc[test_indices]
    y_train, y_test = y.iloc[train_indices], y.iloc[test_indices]

    return X_train, X_test, y_train, y_test


X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2, random_state=1337)


def linear_regression(X, y):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    return theta


def predict(X, theta):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    return X_b @ theta


def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot


# Модель 1: все признаки
theta1 = linear_regression(X_train, y_train)
y_pred1 = predict(X_test, theta1)
r2_1 = r_squared(y_test, y_pred1)
print(f'Коэффициент детерминации для Модели 1: {r2_1:.4f}')

# Модель 2: только географические признаки
geo_features = ['Longitude', 'Latitude']
X_train_geo = X_train[geo_features]
X_test_geo = X_test[geo_features]

theta2 = linear_regression(X_train_geo, y_train)
y_pred2 = predict(X_test_geo, theta2)
r2_2 = r_squared(y_test, y_pred2)
print(f'Коэффициент детерминации для Модели 2: {r2_2:.4f}')

# Модель 3: выбранные признаки + синтетический признак
X_train_synthetic = X_train.copy()
X_test_synthetic = X_test.copy()

X_train_synthetic['RoomsPerHousehold'] = X_train['TotalRooms'] / X_train['Households']
X_test_synthetic['RoomsPerHousehold'] = X_test['TotalRooms'] / X_test['Households']

X_train_synthetic['RoomsPerHousehold'] = X_train_synthetic['RoomsPerHousehold'].replace([np.inf, -np.inf], 0).fillna(0)
X_test_synthetic['RoomsPerHousehold'] = X_test_synthetic['RoomsPerHousehold'].replace([np.inf, -np.inf], 0).fillna(0)

selected_features = ['Longitude', 'Latitude', 'RoomsPerHousehold']
X_train_sel = X_train_synthetic[selected_features]
X_test_sel = X_test_synthetic[selected_features]

theta3 = linear_regression(X_train_sel, y_train)
y_pred3 = predict(X_test_sel, theta3)
r2_3 = r_squared(y_test, y_pred3)
print(f'Коэффициент детерминации для Модели 3: {r2_3:.4f}')

print('\nСравнение коэффициентов детерминации моделей:')
print(f'Модель 1 (все признаки): R^2 = {r2_1:.4f}')
print(f'Модель 2 (географические признаки): R^2 = {r2_2:.4f}')
print(f'Модель 3 (выбранные признаки + синтетический признак): R^2 = {r2_3:.4f}')
