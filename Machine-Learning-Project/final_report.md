## Machine Learning: Classification of Persons of Interest in Enron Dataset
_Last Updated: 4/26/2018_

## Introduction
After the fall of Enron on December 2, 2001, a massive data dump of information was released to the public following the Federal Energy Regulatory Commission's (FERC) investigation into the company. This dataset, known as the "Enron Corpus", contains over 600,000 emails from some of the top leadership at Enron.

In this project, machine learning will be applied to this infamous Enron dataset. The goal is to create a classifier that can accurately identify whether an individual is a person of interest (POI) or not. A "person of interest", in the context of this project, is an individual working at Enron who potentially had insider knowledge on the fraud that was occuring. For example, the CEO of Enron, Jefferey Skilling, would be considered a POI based upon his knowledge of the company and his fate following the investigation.

Machine learning is the core mechanism that allows us to find and classify these POIs. It allows us to comb through thousands of data points and find the hidden relationships between them. These relationships result in being able to make a classifier that can identify whether an individual was a POI or not.

## Exploration of the Dataset
Before a machine learning classifier can be built, the dataset itself needs to be explored. Missing values need to be dealt with, outliers need to be evaluated, and the general structure of the data needs to be reviewed. 

### Basic Characteristics
This section covers to basic characteristics of the dataset:

* Total records: 146
* Number of POIs: 18
* Number of nonPOIs: 128
* Number of features available: 21
* Number of NaNs: 1358

POIs only make up about 12.3% of the dataset. This characteristics is very important. Because the number of POIs is so small, extra care will need to be taken to ensure that the train and test sets have a equal percentage of POIs in both of them. 

### Outliers
Addressing outliers is essential to ensure that the data is being as representative as possible for the classifiers. Howwever, due to the small size of the dataset, outliers should be treated in a very conservative manner. Only outliers that may be due to input error or other collection errors should be removed. 

In order to find extreme outliers, each of the features were plotted as a histogram to view the distribution of the values. An outlier immediately revealed itself in the series of plots. Below is a histrogram of the slaraies of each person in the dataset:

![graph](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/Machine-Learning-Project/images/salary_outlier.png)

Pulling the name of the record that had the max salary showed that the entry was named `'TOTAL'` with a salary of $26,704,229. Because this value is so much higher than any of the others in the distribution, this could be an entry left over when the financial data was imported into the python dictionary.  Because this record is the result of a collection error, the record is removed from the dataset.

After removing the `'TOTAL'` record, replotting the histograms revealed that there did not appear to be any other extreme outliers.

![graph](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/Machine-Learning-Project/images/salary.png)

### Missing Values
Most classifiers will not work if there are `NaNs` present in the training and test data. As such, missing data needs to be dealt with before the dataset can be applied to the machine learning algorithms. 

Fortunately, the built-in function provided by Udacity, `featureFormat`, already addresses any missing values in the dataset. As it retrieves the requested features from the dataset for the classifier, it sets any `NaNs` it encounters to zero. This ensures that every feature has a value and that no errors occur in the classification algorithms due to a missing value.

## Feature Engineering and Selection
### New Features
There were two new features that I made from the Enron dataset. The first one measured the ratio of emails a person recieved that were from POIs. The other measured the ratio of emails a person sent that were to POIs. It would make intuitive sense that a person who is sending and receiving a bunch of emails to and from POIs may be a POI themselves. Individuals with higher than average ratios in one or both of these features may flag them as a POI.

These features were made by dividing the total number of messages from/to a POI by the total number of from/to messages. As an example, imagine that Ken Lay, the founder of Enron, sent a total of 500 emails. Of those 500 emails, 400 of them were to known POIs. Based on these numbers, Ken Lay would have a `from_this_person_to_poi_ratio` of 0.8.

### Feature Selection using SelectKBest
As stated in the 'Basic Characteristics' section, there are a total of 21 features available to use in the classifiers. Adding the two features I created raises the number to 23.  In order to select the best features for the classifiers, SelectKBest was used to identify the most impactful features for the algorithm 

The scores for each of the features, including the newly added features, are listed below:

~~~python
SelectKBest Scores:

[(33, 'bonus'),
 (21, 'salary'),
 (16, 'total_stock_value'),
 (16, 'from_this_person_to_poi_ratio'),
 (15, 'exercised_stock_options'),
 (12, 'long_term_incentive'),
 (11, 'shared_receipt_with_poi'),
 (11, 'deferred_income'),
 (9, 'restricted_stock'),
 (9, 'from_poi_to_this_person'),
 (8, 'total_payments'),
 (6, 'loan_advances'),
 (4, 'expenses'),
 (3, 'other'),
 (3, 'from_this_person_to_poi'),
 (3, 'from_poi_to_this_person_ratio'),
 (2, 'to_messages'),
 (2, 'director_fees'),
 (0, 'restricted_stock_deferred'),
 (0, 'from_messages'),
 (0, 'deferral_payments')]
 ~~~

Trial and error was used to find the right amount of features for the classifcation algorithm. I ultimately decided on using the top five. 
Because `from_this_person_to_poi_ratio` was included in this top five, it was incorporated as a feature in the final algorithm

### Performance of New Features

__Naive Bayes with New Feature__
~~~python
Features used:
  [(22, 'total_stock_value'),
   (22, 'exercised_stock_options'),
   (17, 'bonus'),
   (15, 'salary'),
   (6, 'from_this_person_to_poi_ratio')]

Performance:
  Accuracy: 0.85629       
  Precision: 0.49545    
  Recall: 0.32650 
  F1: 0.39361     
  F2: 0.35040
          Total predictions: 14000        
          True positives:  653  
          False positives:  665   
          False negatives: 1347 
          True negatives: 11335
~~~

This algorithm was tested again, but with the new features removed:

__Naive Bayes without New Feature__
~~~python
Features used:
  [(20, 'total_stock_value'),
   (20, 'exercised_stock_options'),
   (14, 'bonus'),
   (12, 'salary'),
   (8, 'long_term_incentive')]
 
Performance:
  Accuracy: 0.83723       
  Precision: 0.45748    
  Recall: 0.31200 
  F1: 0.37099     
  F2: 0.33319
          Total predictions: 13000        
          True positives:  624 
          False positives:  740   
          False negatives: 1376 
          True negatives: 10260
~~~

All of the imporant metrics were higher when using the new feature in the Naive Bayes classifier.

### Feature Scaling
Sometimes features need to be scaled appropriately in order for the classifiers to treat each feature equally. Some classifiers will break if the features aren't scaled properly.

However, this does not mean that features should always be scaled. Scaling features can reduce the amount of information about the data points, and can reduce the performance of the classifier. This was true for the Naive Bayes classifier, which saw losses in all important metrics when a scaler was used.

## Classifier Selection and Parameter Tuning
The best way I found to find the appropriate classiffier was to simply test them. It was important to realize that each of the classifiers needed different inputs when it came to feature scaling. 

### Classifiers Explored
In total, I experimented with four different classifiers: Naive Bayes, SVMs, Decision Trees and K-Nearest Neighbors.

#### Guassian Naive Bayes
#### Support Vector Matrix
#### Decision Trees
#### K-Nearest Neighbor 

### Hyper-Parameter Tuning using GridSearchCV
In order to find the optimal for each of these classiffiers, GridSearchCv was used. 

## Validation
### What is Validation?
### Types of Validation Used

## Final Evaluation and Performance

## Summary
