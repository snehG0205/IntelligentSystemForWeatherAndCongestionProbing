from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
 

def tempPred():
    series = read_csv('temperature.csv')
    X = series.values
    size = int(len(X) * 0.99)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    
    print("Temperature")

    for t in range(len(test)):
        model = ARIMA(history, order=(12,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print(' %d predicted=%.3f, expected=%.3f' % (t,yhat, obs))
    
   
    print("for next week")
    predictions_week = []
    test_week = predictions[-7:]
    
    for t in range(len(test_week)):
        model = ARIMA(history, order=(12,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions_week.append(yhat)
        obs = test_week[t]
        history.append(obs)
        print('predicted=%.3f, expected=%.3f' % (yhat, obs))
        
        
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)
        
    return(predictions_week)
    
    
    
var = tempPred()
print(var)
