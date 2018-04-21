#!/usr/bin/python

import sys
import numpy as np
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from tester import test_classifier

#########################
### Feature Selection ###
#########################

### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

### Below is a MASTER LIST used for testing:

features_list = ['poi', 'salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees', 'to_messages', 'from_poi_to_this_person', 'from_messages',
'from_this_person_to_poi', 'shared_receipt_with_poi', 'from_poi_to_this_person_ratio', 'from_this_person_to_poi_ratio']

### Final features used in classifier
#features_list = ['poi', 'loan_advances', 'bonus', 'exercised_stock_options',  'from_this_person_to_poi_ratio']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

print("Load dict")

#######################
### Remove outliers ###
#######################

data_dict.pop('TOTAL')

print("Remove outliers")

###########################
### Create new features ###
###########################

# Create 'from_this_person_to_poi_ratio':
for key in data_dict.keys():
    from_p_to_poi = data_dict[key]['from_this_person_to_poi']
    from_messages = data_dict[key]['from_messages']
    if from_p_to_poi == 'NaN':
        to_poi = 0
    if from_messages == 'NaN':
        from_messages = 0
    try:
        data_dict[key]['from_this_person_to_poi_ratio'] = float(from_p_to_poi) / int(from_messages)
    except ZeroDivisionError:
        data_dict[key]['from_this_person_to_poi_ratio'] = 0

# Create 'from_poi_to_this_person_ratio':
for key in data_dict.keys():
    from_poi_to_p = data_dict[key]['from_poi_to_this_person']
    to_messages = data_dict[key]['to_messages']
    if from_poi_to_p == 'NaN':
        from_poi_to_p = 0
    if to_messages == 'NaN':
        to_messages = 0
    try:
        data_dict[key]['from_poi_to_this_person_ratio'] = float(from_poi_to_p) / int(to_messages)
    except ZeroDivisionError:
        data_dict[key]['from_poi_to_this_person_ratio'] = 0

print("Create new features")

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

print("Extracted features and labels")

### Visualization code used for feature exploration
import numpy as np
import matplotlib.pyplot as plt

f1 = []
f2 = []
for ii in features:
    f1.append(ii[0])
    f2.append(ii[1])

fig, ax = plt.subplots()
plt.scatter(f1, f2, s=2, c=labels)
#plt.show()

print("Plotted features")

###################
### Classifiers ###
###################

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
### Different classifiers used for testing
clf_tree = DecisionTreeClassifier()
clf_nb = GaussianNB()
clf_svm = SVC()
clf_kn = KNeighborsClassifier()

print("Created classifiers")

##############################
### Classifier Performance ###
##############################

### Tune your classifier to achieve better than .3 precision and recall
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info:
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

### Split into training and testing sets
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.1, random_state=42)

### Scale data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

### Univariate feature selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
selector = SelectKBest(chi2, k='all')

### PCA
from sklearn.decomposition import PCA
pca = PCA()

### Create Pipeline
from sklearn.pipeline import Pipeline
clf = Pipeline([('scaler', scaler),
                ('SKB', selector),
                ('PCA', pca),
                ('classifier', clf_kn)])
#clf.set_params(PCA__n_components=1, classifier__kernel='rbf', classifier__C=10, classifier__gamma=100000)
#clf.set_params(classifier__min_samples_split=7, classifier__max_depth=None)
clf.fit(features_train, labels_train)
print(np.int64(clf.named_steps['SKB'].scores_))
print([round(i, 2) for i in clf.named_steps['PCA'].explained_variance_ratio_])
print(clf.score(features_test, labels_test))

### GridSearchCV for parameter tuning
from sklearn.model_selection import GridSearchCV
param_svm = dict(PCA__n_components=[2, 4, 6, 8],
                 classifier__C=[1, 10, 100, 1000],
                 classifier__kernel=['linear', 'rbf'],
                 classifier__gamma=['auto', 1, 10, 100, 1000, 10000, 100000])
param_tree = dict(classifier__min_samples_split=[2, 3, 4, 5, 6, 7, 8, 9, 10],
                  classifier__max_depth=[None, 5, 10, 15, 20, 50, 100])
param_kn = dict(PCA__n_components=[2, 4, 6, 8],
                classifier__n_neighbors=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15],
                classifier__leaf_size=[10, 20, 30, 40 , 50])
grid_search = GridSearchCV(clf, param_grid=param_kn)
grid_search.fit(features_train, labels_train)
print(grid_search.best_params_)
print(grid_search.score(features_test, labels_test))

test_classifier(clf, my_dataset, features_list)


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
