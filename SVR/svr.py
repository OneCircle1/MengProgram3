import pandas as pd
import numpy as np
import datetime
from sklearn.svm import SVR
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/cxy/Downloads/tgh/MengProgram3/SVR/ge.us.txt', sep=",", header=0)
# data = pd.read_csv('month.txt', sep=",", header=0)
data.columns = ["Date", "Open", "High", "Low", "Close", "Volume", "OpenInt"]

dates = []
prices = []

data = data.head(len(data)-1)
data_dates = data.loc[:,"Date"]
data_open = data.loc[:, "Open"]

for date in data_dates:
    interval = datetime.datetime(int(date.split('-')[0]),int(date.split('-')[1]),int(date.split('-')[2])) - datetime.datetime(1962,1,2)
    dates.append([int(interval.days+1)])

for open_price in data_open:
    prices.append(float(open_price))

def predict_prices(dates, prices, x):
    # svr_lin = SVR(kernel = 'linear', C = 1e3)
    svr_poly = SVR(kernel = 'poly', C = 1e3, degree = 2)
    svr_rbf = SVR(kernel = 'rbf', C = 1e3, gamma = 0.1)
    
    # svr_lin.fit(dates,prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    rbf_predict = svr_rbf.predict(dates)
    poly_predict = svr_poly.predict(dates)

    rbf_mse=np.sum((rbf_predict-prices)**2)/len(rbf_predict)
    poly_mse=np.sum((poly_predict-prices)**2)/len(poly_predict)
    print("RBF MSE:", rbf_mse)
    print("POLY MSE:", poly_mse)

    rbf_mae=np.sum(np.absolute(rbf_predict-prices))/len(prices)
    poly_mae=np.sum(np.absolute(poly_predict-prices))/len(prices)
    print("RBF MAE:", rbf_mae)
    print("POLY MAE:", poly_mae)
    
    plt.scatter(dates,prices,color = 'black',label = 'Data')
    plt.scatter(dates,rbf_predict,color = 'red',label = 'RBF Model')
    # plt.scatter(dates,svr_lin.predict(dates),color = 'green',label = 'Linear Model')
    plt.scatter(dates,poly_predict,color = 'blue',label = 'Polynominal Model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('SVR')
    plt.legend()
    plt.show()
    
    return svr_rbf.predict(x)[0],svr_poly.predict(x)[0]
    # return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0]

predicted_price = predict_prices(dates, prices, [[20402]])
print(predicted_price)
  
