## Machine Learning: Classification of Persons of Interest in Enron Dataset
_Last Updated: 4/25/2018_

## Introduction
After the fall of Enron on December 2, 2001, a massive data dump of information was released to the public following the Federal Energy Regulatory Commission's (FERC) investigation into the company. This dataset, known as the "Enron Corpus", contains over 600,000 emails from some of the top leadership at Enron.

In this project, machine learning will be applied to this infamous Enron dataset. The goal is to create a classifier that can accurately identify whether an individual is a person of interest (POI) or not. A "person of interest" in the context of this prokect is an individual working at Enron who potentially had insider knowledge on the fraud that was occuring at Enron. For example, the CEO of Enron, Jefferey Skilling, would be considered a POI based upon his knowledge of the company and his fate following the investigation.

Machine learning is the core mechanism that allows us to find and classify these POIs. It allows us to comb through thousands of data points and find the hidden relationships between them. These relationships result in being able to make a classifier that can identify whether an individual was a POI or not.

## Exploration of the Dataset
Before a machine learning classifier can be built, the dataset itself needs to be explored. Missing values need to be dealt with, outliers need to be evaluated, and the general structure of the data needs to be reviewed. 

### Basic Characteristics
This section covers to basic characteristics of the dataset:
* Total records: 146
* Number of POIs: 18
* Number of nonPOIs: 128
* Number of features available: 21

### Outliers
Addressing outliers is essential to ensure that the data is being as representative as possible for the classifiers. Howwever, due to the small size of the dataset, outliers should be treated in a very conservative manner. Only outliers that may be due to input error or other collection errors should be removed. 

In order to find extreme outliers, each of the featuers were plotted as histograms to view the distribution of the values. An outlier immediately revealed itself in the series of plots. 

![graph](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/Machine-Learning-Project/images/salary_outlier.png)

Pulling the name of the record that had the max for these features showed that the entry was named `'TOTAL'`. Because this value is so much higher than any of the others in the distribution, this could be an entry left over when the financial data was imported into the python dictionary.  Because this record is the result of a collection error, the reocrd is removed from the dataset.

After removing the `'TOTAL'` records, replotting the histograms revealed that there did not appear to be any other extreme outliers.

![graph](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/Machine-Learning-Project/images/salary.png)

### Missing Values
Most classifiers will not work if there are `NaNs` present in teh training and test data. As such, missing data needs to be dealt with before the dataset can be applied to the algorithms. 

Fortunately, the built in function provided by Udacity, `featureFormat`, already addresses any missing values in the dataset. As it retrives the requested features from the dataset for the classifier, it sets an `NaNs` it encounters by setting them to zero. This ensures that every feature has a value and that no errors occur in the classification algorithms.

## Feature Engineering and Selection
### New Features
### Feature Selection using SelectKBest
### Feature Scaling

## Classifier Selection and Parameter Tuning
### Classifiers Explored
### Hyper-Parameter Tuing using GridSearchCV

## Validation
### What is Validation?
### Types of Validation Used

## Final Evaluation and Performance

## Summary
