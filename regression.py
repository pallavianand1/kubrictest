# -*- coding: utf-8 -*-
"""regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/179vD0nw86f4yx4kMJ-aJIQKMOvZ7FEOi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

data = pd.read_csv('/content/linreg_train.csv')

x_train = data['area']
y_train = data['price']



from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

from scipy.stats import linregress
linregress(x_train, y_train)

plt.scatter(x_train, y_train)

m = 0.03446688454635256
c = 1153.0968977289224
y = m * x_train + c
plt.plot(x_train, y, color='#58b970', label='Regression Line')
plt.scatter(x_train, y_train, label='Price Prediction')
plt.xlabel('area')
plt.ylabel('price')
plt.legend()

from sklearn.metrics import r2_score
print (r2_score)