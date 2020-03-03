# MengProgram3
Time series analysis.

[link](https://en.wikipedia.org/wiki/Time_series)

# Background

We can use time series to make prediction.

# Requirement
* Drawing curve of daily high and daily volume.
* Use SVR, ARIMA, LSTM to do fitting and forecasting. 
* Calculate the prefermance of each altorithm, such as MAE and MSE.

# Result

### Visualization

![image](https://github.com/OneCircle1/MengProgram3/blob/master/visualization/png/Volume.png)

![image](https://github.com/OneCircle1/MengProgram3/blob/master/visualization/png/HL.png)

### SVR

The MSE and MAE of two models

```
RBF MSE: 0.01158638260458696
POLY MSE: 54.33059841213097
RBF MAE: 0.0926518995279471
POLY MAE: 4.396930495455487
```

![image](https://github.com/OneCircle1/MengProgram3/blob/master/SVR/png/SVR.png)

### ARIMA

```python 
MSE: 0.142
MAE: 37.443
```

![image](https://github.com/OneCircle1/MengProgram3/blob/master/ARIMA/png/ARIMA.png)

### LSTM

```python
MSE: 0.29673335476669743
MAE: 0.3973067512257079
```

![image](https://github.com/OneCircle1/MengProgram3/blob/master/LSTM/png/LSTM.png)

# Milestone
Let it go.
