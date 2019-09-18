####################
# Step - By - Step Guide Machine Learning in Python
####################

#import libraries

## Libraries for statistical analysis and visualizations

import sys
# scipy
import scipy
# numpy
import numpy
# matplotlib
import matplotlib
# pandas
import pandas
# scikit-learn
import sklearn

## Libraries for algorithms and functions

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# In this we will use iris data set. It is like the "hello world" of data sets

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#Analyze Data Set

# shape
print(dataset.shape)s

# You should see 150 instances and 5 attributes
# Let's see this


# This will print out the first 20 rows of data
print(dataset.head(20))

# Get a statistical summary: mean, count, standard deviation, min, max
print(dataset.describe())

# Breakdown variables by class: how many of each?
# aka class distribution
print(dataset.groupby('class').size())

# Let's Visualize our dataset
#Univariate visualizations

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

#Multivariate plots

# scatter plot matrix
scatter_matrix(dataset)
plt.show()

#Here's the random forest code, kinda messy, but works. You'll get a warning, which is ok. Visualizing features next comment.

from sklearn.ensemble import RandomForestClassifier

# Create decision tree classifer object
clf = RandomForestClassifier(random_state=0, n_jobs=-1)

# Train model
model = clf.fit(X_train, Y_train)

# Calculate feature importances
importances = model.feature_importances_

predictions = model.predict(X_validation)
print(model.score(X_validation, Y_validation)) # (NOT good)

# Sort feature importances in descending order
indices = np.argsort(importances)[::-1]

# Rearrange feature names so they match the sorted feature importances
#names = [iris.feature_names[i] for i in indices]
names = [feature_name for feature_name in dataset.columns]

# Create plot
plt.figure()

# Create plot title
plt.title("Feature Importance")

# Add bars
plt.bar(range(X.shape[1]), importances[indices])

# Add feature names as x-axis labels
plt.xticks(range(X.shape[1]), names, rotation=90)

# Show plot
plt.show()

#Evaluate Algorithms
# We will split the loaded dataset into two:
# 80% of which we will use to train our models and 20% that we will hold back as a validation dataset.

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# You now have training data in the X_train and Y_train for preparing models and a X_validation and Y_validation sets that we can use later.

# Set up 10- fold test harness
# This will split our dataset into 10 parts, train on 9 and test on 1 and repeat for all combinations of train-test splits.

# Test options and evaluation metric
seed = 7 # The specific random seed does not matter, learn more about pseudorandom number generators here:
scoring = 'accuracy' # We are using the metric of ‘accuracy‘ to evaluate models.

# Build and Evaluate Models

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn

results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


# Make Predictions
# Make predictions on validation dataset

knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))