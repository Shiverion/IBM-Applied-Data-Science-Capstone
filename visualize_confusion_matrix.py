
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

def plot_confusion_matrix(y, y_predict):
    "this function plots the confusion matrix"
    cm = confusion_matrix(y, y_predict)
    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax, cmap='Blues', fmt='d') # annot=True to annotate cells
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix - Decision Tree') # Updated title
    ax.xaxis.set_ticklabels(['did not land', 'land'])
    ax.yaxis.set_ticklabels(['did not land', 'landed'])
    plt.savefig('images/confusion_matrix.png', bbox_inches='tight')
    plt.close()

# Load data
print("Loading data...")
data = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
X = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv")

# Create Y
Y = data['Class'].to_numpy()

# Standardize X
transform = preprocessing.StandardScaler()
X = transform.fit_transform(X)

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Define Decision Tree parameters for GridSearchCV
parameters = {
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_depth': [2*n for n in range(1,10)],
    'max_features': ['sqrt'], # 'auto' is deprecated/removed in newer sklearn, using 'sqrt' which is equivalent or similar for this context
    'min_samples_leaf': [1, 2, 4],
    'min_samples_split': [2, 5, 10]
}

# Create and fit GridSearchCV
print("Training Decision Tree with GridSearchCV...")
tree = DecisionTreeClassifier(random_state=2) # Added random_state for reproducibility
tree_cv = GridSearchCV(tree, parameters, scoring='accuracy', cv=10)
tree_cv.fit(X_train, Y_train)

print("Best Parameters:", tree_cv.best_params_)
print("Accuracy on Test Data:", tree_cv.score(X_test, Y_test))

# Predict and plot confusion matrix
yhat = tree_cv.predict(X_test)
plot_confusion_matrix(Y_test, yhat)
print("Confusion matrix saved to images/confusion_matrix.png")

# Save results to text file
with open('confusion_matrix_results.txt', 'w') as f:
    f.write(f"Best Parameters: {tree_cv.best_params_}\n")
    f.write(f"Accuracy on Test Data: {tree_cv.score(X_test, Y_test)}\n")
    cm = confusion_matrix(Y_test, yhat)
    f.write(f"Confusion Matrix:\n{cm}\n")

