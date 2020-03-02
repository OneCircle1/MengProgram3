# SVR

As in classification, support vector regression (SVR) is characterized by the use of kernels, sparse solution, and VC control of the margin and the number of support vectors. Although less popular than SVM, SVR has been proven to be an effective tool in real-value function estimation.

# Instruction

Install pandas, numpy, sklearn, matplotlib, python3.

Run SVR.py.

# Result

After observation, linear model can not be used in this project. So two other prediction models are used in the project. One is RBF model, and the other is polynominal models. It is quite obvious that RBF model is more precise.



The MSE and MAE of two models

```
RBF MSE: 0.01158638260458696
POLY MSE: 54.33059841213097
RBF MAE: 0.0926518995279471
POLY MAE: 4.396930495455487
```



![image](https://github.com/OneCircle1/MengProgram3/blob/master/SVR/png/SVR.png)



The real stock price on ```2017-11-10``` is ```19.98```. The first number below is the price predicted with RBF model, and the second number below is the price predicted with polynominal models.

```python
(18.908096023495467, 26.8017842384543)
```

