#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees', 'to_messages',  'from_poi_to_this_person', 'from_messages',
'from_this_person_to_poi', 'shared_receipt_with_poi'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

print("Load dict")

### Task 2: Remove outliers
data_dict.pop('TOTAL')

print("Remove outliers")

### Task 3: Create new feature(s)
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
#print(my_dataset['METTS MARK'])
#print(len(my_dataset))

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)
print("Extracted features and labels")

### Plotting code for feature exploration
import numpy as np
import matplotlib.pyplot as plt

f1 = []
f2 = []
for ii in features:
    f1.append(ii[0])
    f2.append(ii[1])
f1 = np.array(f1)
f2 = np.array(f2)

fig, ax = plt.subplots()
plt.scatter(f1, f2, s=2, c=labels)
plt.show()

print("Plotted features")

### Scale data


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
features = scaler.fit_transform(features)


### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(min_samples_split=2)
clf1 = GaussianNB()
clf1 = LinearSVC()

print("Created classifiers")

### Task 5: Tune your classifier to achieve better than .3 precision and recall
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info:
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Recursive feature slection for LinearSVM experimentation
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
#refcv = RFECV(estimator=clf, cv=StratifiedKFold(2), scoring='accuracy')
#refcv.fit(features, labels)
#print(refcv.n_features_)

# Univariate feature selection for Naive Bayes
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
selector = SelectKBest(chi2, k='all').fit(features, labels)
features = selector.transform(features)
scores = selector.scores_

print("Performed feature selection")

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.2, random_state=42)



clf.fit(features_train, labels_train)
score = clf.score(features_test, labels_test)
print(score)


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
