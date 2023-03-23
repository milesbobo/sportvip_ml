import numpy as np
import  pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston_datasets = load_boston()
print(boston_datasets.keys())
print(boston_datasets.data)#等价于boston_datasets['data']

x_train,x_test,y_train,y_test = train_test_split(boston_datasets.data,boston_datasets.target,random_state = 0,train_size = 0.75)

boston_lr = LinearRegression()
boston_lr.fit(x_train,y_train)

print(boston_lr.score(x_train,y_train))
print(boston_lr.score(x_test,y_test))
#print(f"{boston_lr.coef_}",)
#print(boston_lr.intercept_)

from sklearn.linear_model import Ridge

boston_ridge = Ridge(alpha = 0.5)
boston_ridge.fit(x_train,y_train)
print(boston_ridge.score(x_train,y_train))
print(boston_ridge.score(x_test ,y_test ))

