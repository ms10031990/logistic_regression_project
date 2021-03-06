# Default Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.logistic_regression_project.q01_outlier_removal.build import outlier_removal
from sklearn.preprocessing import Imputer

loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)
loan_data = outlier_removal(loan_data)

def data_cleaning(data):
    X = data.iloc[:,:-1]
    y = data['Loan_Status']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, test_size=0.25)

    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(X_train[['LoanAmount']])
    X_train['LoanAmount'] = imp_mean.transform(X_train[['LoanAmount']])

    imp_mean.fit(X_test[['LoanAmount']])
    X_test['LoanAmount'] = imp_mean.transform(X_test[['LoanAmount']])

    X_train['Gender'] = X_train['Gender'].fillna(X_train['Gender'].mode()[0])
    X_train['Married'] = X_train['Married'].fillna(X_train['Married'].mode()[0])
    X_train['Dependents'] = X_train['Dependents'].fillna(X_train['Dependents'].mode()[0])
    X_train['Self_Employed'] = X_train['Self_Employed'].fillna(X_train['Self_Employed'].mode()[0])
    X_train['Loan_Amount_Term'] = X_train['Loan_Amount_Term'].fillna(X_train['Loan_Amount_Term'].mode()[0])
    X_train['Credit_History'] = X_train['Credit_History'].fillna(X_train['Credit_History'].mode()[0])

    X_test['Gender'] = X_test['Gender'].fillna(X_test['Gender'].mode()[0])
    X_test['Married'] = X_test['Married'].fillna(X_test['Married'].mode()[0])
    X_test['Dependents'] = X_test['Dependents'].fillna(X_test['Dependents'].mode()[0])
    X_test['Self_Employed'] = X_test['Self_Employed'].fillna(X_test['Self_Employed'].mode()[0])
    X_test['Loan_Amount_Term'] = X_test['Loan_Amount_Term'].fillna(X_test['Loan_Amount_Term'].mode()[0])
    X_test['Credit_History'] = X_test['Credit_History'].fillna(X_test['Credit_History'].mode()[0])

    return X,y,X_train,X_test,y_train,y_test

''' Optimized way
def data_cleaning(data):
    #find X and y
    X,y = data.loc[:, data.columns != 'Loan_Status'], data[ 'Loan_Status']

    #split train-test (25% test)
    X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.25, random_state=9)

    num_features =['LoanAmount']
    cat_features=['Gender', 'Married', 'Dependents', 'Self_Employed', 'Loan_Amount_Term', 'Credit_History']

    #find mean of train for numeric features
    for col in num_features:
        mean_train= X_train[col].mean()
        #impute missing data in train and test  with mean
        X_train.loc[:,col]=X_train[col].fillna(mean_train)
        X_test.loc[:,col]=X_test[col].fillna(mean_train)

    for col in cat_features:
        #find mode of train data for categorical features
        mode_train= X_train[col].mode()[0]
        #impute missing data in train and test  with mode
        X_train.loc[:,col]=X_train[col].fillna(mode_train)
        X_test.loc[:,col]=X_test[col].fillna(mode_train)

    return X,y,X_train,X_test,y_train,y_test
'''
