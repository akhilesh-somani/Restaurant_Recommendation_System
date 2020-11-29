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

def evaluate_rate_model(model, Review_test, Label_test, num_thread):
    """
    Return: score of each test rating.
    """
    
    users,items = [],[]
    for i in range(len(Review_test)):
        users.append(Review_test[i][0])
        items.append(Review_test[i][1])
        
    predictions = model.predict([np.array(users), np.array(items)], batch_size=1000, verbose=0)

    y_test = np.array(Label_test)*5
    yhat = np.array(predictions)*5
    assert len(predictions) == len(Label_test)
    mse = mean_squared_error(y_test, yhat)
    r2 = r2_score(y_test, yhat)
    
    return (mse, r2)
