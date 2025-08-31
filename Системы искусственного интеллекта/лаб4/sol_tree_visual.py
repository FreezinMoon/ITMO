import pandas as pd
import numpy as np
import math

# === Data Loading and Preprocessing ===

# Load data
data = pd.read_csv('agaricus-lepiota.data', header=None)

# Assign column names
data.columns = ['class'] + ['feature_' + str(i) for i in range(1, data.shape[1])]

# Number of features (excluding the class label)
n_features = data.shape[1] - 1

# Calculate sqrt(n) and randomly select features
k = int(math.sqrt(n_features))
np.random.seed(42)  # For reproducibility
selected_features = np.random.choice(data.columns[1:], size=k, replace=False)

# Create a new DataFrame with selected features and class label
data_selected = data[['class'] + list(selected_features)]

# === Defining the TreeNode Class ===

class TreeNode:
    def __init__(self, feature=None, children=None, is_leaf=False, prediction=None, probabilities=None):
        self.feature = feature
        self.children = children if children is not None else {}
        self.is_leaf = is_leaf
        self.prediction = prediction
        self.probabilities = probabilities

# === Functions for Building the Tree ===

# Entropy calculation
def entropy(s):
    counts = s.value_counts()
    probabilities = counts / counts.sum()
    return -sum(probabilities * np.log2(probabilities + 1e-9))  # Adding epsilon to avoid log(0)

# Information gain calculation
def information_gain(data, feature, target_attribute_name='class'):
    total_entropy = entropy(data[target_attribute_name])
    vals, counts = np.unique(data[feature], return_counts=True)
    weighted_entropy = 0
    for val, count in zip(vals, counts):
        subset = data[data[feature] == val]
        weighted_entropy += (count / data.shape[0]) * entropy(subset[target_attribute_name])
    return total_entropy - weighted_entropy

# Building the decision tree
def build_tree(data, features, target_attribute_name='class'):
    # Base Cases
    if len(np.unique(data[target_attribute_name])) == 1:
        prediction = data[target_attribute_name].iloc[0]
        probabilities = {prediction: 1.0}
        return TreeNode(is_leaf=True, prediction=prediction, probabilities=probabilities)
    elif len(features) == 0:
        counts = data[target_attribute_name].value_counts(normalize=True)
        prediction = counts.idxmax()
        probabilities = counts.to_dict()
        return TreeNode(is_leaf=True, prediction=prediction, probabilities=probabilities)
    else:
        # Selecting the Best Feature
        gains = [information_gain(data, feature) for feature in features]
        best_feature_index = np.argmax(gains)
        best_feature = features[best_feature_index]
        tree = TreeNode(feature=best_feature)
        # Splitting the Data
        feature_values = np.unique(data[best_feature])
        features = [f for f in features if f != best_feature]
        for value in feature_values:
            subset = data[data[best_feature] == value]
            if subset.empty:
                counts = data[target_attribute_name].value_counts(normalize=True)
                prediction = counts.idxmax()
                probabilities = counts.to_dict()
                subtree = TreeNode(is_leaf=True, prediction=prediction, probabilities=probabilities)
            else:
                subtree = build_tree(subset, features.copy(), target_attribute_name)
            tree.children[value] = subtree
        return tree

# === Prediction Function ===

def predict_proba(instance, tree):
    if tree.is_leaf:
        return tree.probabilities
    else:
        feature_value = instance[tree.feature]
        if feature_value in tree.children:
            return predict_proba(instance, tree.children[feature_value])
        else:
            # If the feature value was not seen during training
            counts = train_data['class'].value_counts(normalize=True)
            return counts.to_dict()

# === Tree Printing Function ===
def print_tree(node, depth=0):
    prefix = "|   " * depth
    if node.is_leaf:
        print(f"{prefix}Leaf: Prediction = {node.prediction}, Probabilities = {node.probabilities}")
    else:
        for value, child in node.children.items():
            print(f"{prefix}{node.feature} = {value}")
            print_tree(child, depth + 1)

# === Main Execution ===

# Splitting the data into training and testing sets
data_selected = data_selected.sample(frac=1, random_state=42).reset_index(drop=True)
train_size = int(0.8 * data_selected.shape[0])
train_data = data_selected.iloc[:train_size]
test_data = data_selected.iloc[train_size:]

# Building the decision tree
features = list(train_data.columns[1:])  # Exclude the class label
tree = build_tree(train_data, features)

# Print the decision tree
print_tree(tree)