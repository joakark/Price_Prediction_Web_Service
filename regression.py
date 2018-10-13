import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def run_regression(inputs):

    housing = pd.read_csv("housing.csv")

    X = housing.loc[:, 'crime_rate':'pupil_teacher_ratio'].values
    y = np.log(housing.house_value)

    lr = LinearRegression()
    model = lr.fit(X, y)
    y_pred = lr.predict(X)
    stddev = round(np.sqrt(mean_squared_error(y,y_pred)),2)

    X_test = []

    for name in inputs:
       X_test.append(inputs[name])

    prediction = lr.predict(np.array(X_test).reshape(1,-1))
    prediction = round(np.exp(prediction).tolist()[0],2)

    results = {"house_value": prediction,
               "stddev": stddev}

    return results
