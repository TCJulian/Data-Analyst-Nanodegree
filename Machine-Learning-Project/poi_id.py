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

#features_list = ['poi', 'salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees', 'to_messages', 'from_poi_to_this_person', 'from_messages',
#'from_this_person_to_poi', 'shared_receipt_with_poi', 'from_poi_to_this_person_ratio', 'from_this_person_to_poi_ratio']

### Final features used in classifier
features_list = ['poi', 'salary', 'bonus', 'total_stock_value', 'exercised_stock_options', 'long_term_incentive']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

#######################
### Remove outliers ###
#######################

data_dict.pop('TOTAL')

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

#################################################
### Data Extraction and Feature Visualization ###
#################################################

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Visualization code used for univariate feature exploration
import matplotlib.pyplot as plt

for i in range(0, len(features_list)-1):
    f1 = []
    for ii in features:
        f1.append(ii[i])

    fig, ax = plt.subplots()
    ax.hist(f1, 30)
    ax.set_title(features_list[i+1])
    #plt.show()
    plt.close('all')

###################
### Classifiers ###
###################

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

### Different classifiers used for testing
clf_nb = GaussianNB()
clf_svm = SVC()
clf_tree = DecisionTreeClassifier()
clf_knn = KNeighborsClassifier()

##############################
### Classifier Performance ###
##############################

### Split into training and testing sets
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.1, random_state=42)

### Scale data
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
minmax = MinMaxScaler()
normal = Normalizer()

### Univariate feature selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
selector = SelectKBest(k=5)

### Explore feature scores for feature selection
from sklearn.pipeline import Pipeline
pipe = Pipeline([('SKB', selector),
                 ('classifier', clf_nb)])

pipe.fit(features_train, labels_train)
s = np.int64(pipe.named_steps['SKB'].scores_)
f_scores = [(v, features_list[int(i[0])+1]) for i, v in np.ndenumerate(s)]
print(sorted(f_scores, reverse=True)[:10])

# function
def run_classifier(classifier, params, scaler=None):
    pipe = Pipeline([('scaler', scaler),
                     ('classifier', classifier)])
    cv = StratifiedShuffleSplit(n_splits=5, random_state=42)
    grid_search = GridSearchCV(pipe, param_grid=params, cv=cv, scoring='f1')
    grid_search.fit(features, labels)
    clf = grid_search.best_estimator_
    print(grid_search.best_params_)
    test_classifier(clf, my_dataset, features_list)

### GridSearchCV for hyper-parameter tuning
from sklearn.model_selection import GridSearchCV
param_nb = dict()
param_svm = dict(classifier__C=[1, 10, 100, 1000],
                 classifier__kernel=['linear', 'rbf'],
                 classifier__gamma=['auto', 1, 100, 100000])
param_tree = dict(classifier__min_samples_split=range(2, 11),
                  classifier__max_depth=[None, 5, 10, 15, 20, 50, 100])
param_knn = dict(classifier__n_neighbors=range(1, 25),
                 classifier__leaf_size=range(10, 110, 10),
                 classifier__metric=['euclidean', 'manhattan', 'minkowski'])

run_classifier(clf_knn, param_knn, minmax)


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

#dump_classifier_and_data(clf, my_dataset, features_list)
