# Data Classification of Health Based on Survey Data

This is a project that uses the following machine learning models to classify the health status of an individual based on the given data [here](data/train.csv)

- [Simple Neural Networks](murphy/neural/neural.ipynb)
- [k Nearest Neighbours](murphy/kNN/kNearestNeighbours.ipynb)
- [Naive Bayesian](murphy/NaiveBayes/nb.ipynb)
- [XGBoost](murphy/XGboost/xgboost.ipynb)
- [Random Forest](murphy/randomforest/randomforest.ipynb)

## Preprocessing

Preprocessing notebook can be found [here](murphy/preprocessing/variable_preprocessing.ipynb)

The folllowing methods were used:

1. Remove data with >90% missing data
2. Remove unnecessary predictor variables (there were more than 100)
3. Scale numerical values to between 0 and 1 



