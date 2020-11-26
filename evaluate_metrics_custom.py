'''
Created on Apr 15, 2016
Evaluate the performance of Top-K recommendation:
    Protocol: leave-1-out evaluation
    Measures: Hit Ratio and NDCG
    (more details are in: Xiangnan He, et al. Fast Matrix Factorization for Online Recommendation with Implicit Feedback. SIGIR'16)

@author: hexiangnan
'''

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X, y, num_thread):
    """
    Return: score of each test rating.
    """
    X = np.array(X)
    users = X.T[0]
    items = X.T[1]
    fans = X.T[2]
        
    predictions = model.predict([users, items, fans], batch_size=1000, verbose=0)

    y_actual = np.array(y) * 5
    y_pred = np.array(predictions) * 5
    assert len(y_pred) == len(y_actual)
    mse = mean_squared_error(y_actual, y_pred)
    r2 = r2_score(y_actual, y_pred)
    
    return (mse, r2)
