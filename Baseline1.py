#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import mean_squared_error, r2_score

def baseline1(data, verbose = True):
    df = data.copy()

    # only consider restaurants which have atleast 10 reviews
    df_review = df.groupby("name").filter(lambda x: len(x) >= 10)

    # Create test, train datasets
    np.random.seed(123)
    mask = np.random.rand(len(df_review)) < 0.8

    rest_train_data = df_review[mask]  # restaurant train data
    rest_test_data = df_review.iloc[~mask]  # restaurant test data
    X_test, y_test = rest_test_data.drop('stars', axis=1), rest_test_data.stars

    assert len(rest_test_data) + len(rest_train_data) == len(df_review), 'lengths of test-train and orginal data do not match'
    if verbose == True:
        print('Successfully created train-test data (80:20)')

    # Use train data to create crosstab
    rating_crosstab = rest_train_data.pivot_table(values='stars', index='user_id', columns='name', fill_value=0)
    # display(rating_crosstab.head(3))
    X = rating_crosstab.values.T
    if verbose == True:
        print('Successfully created pivot table for train data')

    avg_rating = rest_train_data.groupby('name')['stars'].mean().sort_values(ascending=False)
    if verbose == True:
        print('Successfully created avg rating for train data')

    SVD = TruncatedSVD(n_components=12, random_state=17)
    result_matrix = SVD.fit_transform(X)
    corr_matrix = np.corrcoef(result_matrix)

    if verbose == True:
        print('Successfully performed SVD')

    restaurant_names = rating_crosstab.columns
    restaurants_list = list(restaurant_names)

    res=[]

    def compute(row):
        name = row["name"]
        rest = restaurants_list.index(name)
        corr_popular_rest = corr_matrix[rest]

        try:
            rest_rate = avg_rating.loc[restaurant_names[np.argmax(corr_popular_rest)]]
            res.append(rest_rate)

        except KeyError:
            res.append(3)

    X_test.apply(compute, axis=1)
    if verbose == True:
        print('Successfully completed test data predictions')

    yhat = res
    assert len(yhat) == len(y_test), 'something went wrong in predicting ratings: lengths do not match'

    d = mean_squared_error(y_test, yhat)
    r2 = r2_score(y_test, yhat)
    print('Root Mean Squared Error is:', np.sqrt(d))
    print('r^2 score is:', r2)

    return d, r2