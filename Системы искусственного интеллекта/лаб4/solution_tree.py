import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# === Шаг 1: Загрузка данных и случайный выбор √n признаков ===
data = pd.read_csv('agaricus-lepiota.data', header=None)

data.columns = ['class'] + ['feature_' + str(i) for i in range(1, data.shape[1])]

n_features = data.shape[1] - 1

k = int(np.sqrt(n_features))
selected_features = np.random.choice(data.columns[1:], size=k, replace=False)

data_selected = data[['class'] + list(selected_features)]


# === Шаг 2: Реализация дерева решений ===

class Node:
    def __init__(self, feature=None, children=None, is_leaf=False, prediction=None, probabilities=None):
        self.feature = feature
        self.children = children if children is not None else {}
        self.is_leaf = is_leaf
        self.prediction = prediction
        self.probabilities = probabilities


def entropy(s):
    counts = s.value_counts()
    probabilities = counts / counts.sum()
    return -sum(probabilities * np.log2(probabilities))


def information_gain(data, feature, target_attribute_name='class'):
    total_entropy = entropy(data[target_attribute_name])
    vals, counts = np.unique(data[feature], return_counts=True)
    weighted_entropy = 0
    for val, count in zip(vals, counts):
        subset = data[data[feature] == val]
        weighted_entropy += (count / data.shape[0]) * entropy(subset[target_attribute_name])
    return total_entropy - weighted_entropy

def split_info(data, feature):
    vals, counts = np.unique(data[feature], return_counts=True)
    probabilities = counts / counts.sum()
    return -sum(probabilities * np.log2(probabilities))

def information_gain_ratio(data, feature, target_attribute_name='class'):
    info_gain = information_gain(data, feature, target_attribute_name)
    split_information = split_info(data, feature)
    # Защита от деления на ноль
    return info_gain / split_information if split_information != 0 else 0


def build_tree(data, features, target_attribute_name='class'):
    # Если все объекты принадлежат одному классу
    if len(np.unique(data[target_attribute_name])) == 1:
        prediction = data[target_attribute_name].iloc[0]
        probabilities = {prediction: 1.0}
        return Node(is_leaf=True, prediction=prediction, probabilities=probabilities)
    # Если больше нет признаков для разделения
    elif len(features) == 0:
        counts = data[target_attribute_name].value_counts(normalize=True)
        prediction = counts.idxmax()
        probabilities = counts.to_dict()
        return Node(is_leaf=True, prediction=prediction, probabilities=probabilities)
    else:
        # Выбор признака с наибольшим приростом информации
        gains = [information_gain_ratio(data, feature) for feature in features]
        best_feature_index = np.argmax(gains)
        best_feature = features[best_feature_index]
        tree = Node(feature=best_feature)
        # Разделение данных по значениям признака
        feature_values = np.unique(data[best_feature])
        features = [f for f in features if f != best_feature]
        for value in feature_values:
            subset = data[data[best_feature] == value]
            if subset.shape[0] == 0:
                counts = data[target_attribute_name].value_counts(normalize=True)
                prediction = counts.idxmax()
                probabilities = counts.to_dict()
                subtree = Node(is_leaf=True, prediction=prediction, probabilities=probabilities)
            else:
                subtree = build_tree(subset, features.copy(), target_attribute_name)
            tree.children[value] = subtree
        return tree


def predict_proba(instance, tree):
    if tree.is_leaf:
        return tree.probabilities
    else:
        feature_value = instance[tree.feature]
        if feature_value in tree.children:
            return predict_proba(instance, tree.children[feature_value])
        else:
            # Если значение признака не встречалось в обучении
            counts = train_data['class'].value_counts(normalize=True)
            return counts.to_dict()


# === Шаг 3: Оценка алгоритма с использованием Accuracy, Precision и Recall ===

def accuracy(y_true, y_pred):
    correct = sum(y_t == y_p for y_t, y_p in zip(y_true, y_pred))
    return correct / len(y_true)

def confusion_matrix(y_true, y_pred, positive_class):
    TP = sum((y_t == positive_class) and (y_p == positive_class) for y_t, y_p in zip(y_true, y_pred))
    FP = sum((y_t != positive_class) and (y_p == positive_class) for y_t, y_p in zip(y_true, y_pred))
    FN = sum((y_t == positive_class) and (y_p != positive_class) for y_t, y_p in zip(y_true, y_pred))
    TN = sum((y_t != positive_class) and (y_p != positive_class) for y_t, y_p in zip(y_true, y_pred))
    return TP, FP, FN, TN

def precision_score(TP, FP):
    return TP / (TP + FP) if (TP + FP) > 0 else 0


def recall_score(TP, FN):
    return TP / (TP + FN) if (TP + FN) > 0 else 0


# === Шаг 4: Построение кривых AUC-ROC и AUC-PR ===

def compute_roc_curve(y_true, y_scores, positive_class='p'):
    thresholds = sorted(set(y_scores), reverse=True)
    tpr_list = []
    fpr_list = []
    for threshold in thresholds:
        y_pred = [positive_class if score >= threshold else 'e' for score in y_scores]
        TP, FP, FN, TN = confusion_matrix(y_true, y_pred, positive_class)
        TPR = TP / (TP + FN) if (TP + FN) > 0 else 0
        FPR = FP / (FP + TN) if (FP + TN) > 0 else 0
        tpr_list.append(TPR)
        fpr_list.append(FPR)
    return fpr_list, tpr_list, thresholds

def compute_pr_curve(y_true, y_scores, positive_class='p'):
    thresholds = sorted(set(y_scores), reverse=True)
    precision_list = []
    recall_list = []
    for threshold in thresholds:
        y_pred = [positive_class if score >= threshold else 'e' for score in y_scores]
        TP, FP, FN, TN = confusion_matrix(y_true, y_pred, positive_class)
        Precision = precision_score(TP, FP)
        Recall = recall_score(TP, FN)
        precision_list.append(Precision)
        recall_list.append(Recall)
    return recall_list, precision_list, thresholds

def compute_auc(x, y):
    auc = 0.0
    for i in range(1, len(x)):
        auc += (x[i] - x[i - 1]) * (y[i] + y[i - 1]) / 2
    return auc


# === Основной блок выполнения ===

data_selected = data_selected.sample(frac=1, random_state=42).reset_index(drop=True)
train_size = int(0.8 * data_selected.shape[0])
train_data = data_selected.iloc[:train_size]
test_data = data_selected.iloc[train_size:]

features = list(train_data.columns[1:])
tree = build_tree(train_data, features)

y_true = test_data['class'].values
y_pred = []
y_scores = []

for index, row in test_data.iterrows():
    probabilities = predict_proba(row, tree)

    prediction = max(probabilities, key=probabilities.get)
    y_pred.append(prediction)

    prob_p = probabilities.get('p', 0)
    y_scores.append(prob_p)

positive_class = 'p'
TP, FP, FN, TN = confusion_matrix(y_true, y_pred, positive_class)
acc = accuracy(y_true, y_pred)
prec = precision_score(TP, FP)
rec = recall_score(TP, FN)

print(f'Accuracy: {acc}')
print(f'Precision: {prec}')
print(f'Recall: {rec}')

fpr_list, tpr_list, roc_thresholds = compute_roc_curve(y_true, y_scores)
roc_data = sorted(zip(fpr_list, tpr_list))
fpr_sorted, tpr_sorted = zip(*roc_data)
roc_auc = compute_auc(fpr_sorted, tpr_sorted)

recall_list, precision_list, pr_thresholds = compute_pr_curve(y_true, y_scores)
pr_auc = compute_auc(recall_list, precision_list)

print(f'ROC AUC: {roc_auc}')
print(f'PR AUC: {pr_auc}')

# === Построение графиков ROC и PR ===
# ROC AUC
plt.figure(figsize=(10, 5))
plt.plot(fpr_sorted, tpr_sorted, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()
# PR AUC
plt.figure(figsize=(10, 5))
plt.plot(recall_list, precision_list, label=f'Precision-Recall Curve (AUC = {pr_auc:.2f})')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='lower left')
plt.show()