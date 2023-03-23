import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
import matplotlib.pyplot as plt

iris_datasets = load_iris()

#print(type(iris_datasets))#Bunch对象类似字典。
print(iris_datasets.keys())
#print(iris_datasets['DESCR'])
#print(iris_datasets['data'])

x_train,x_test,y_train,y_test = train_test_split(iris_datasets["data"],iris_datasets["target"],random_state = 0,train_size = 0.25)
#print(x_train.shape)
#print(y_train.shape)

#散点图：
iris_dateframe = pd.DataFrame(x_train,columns=iris_datasets.feature_names)
print(iris_dateframe.head())

#KNN分类
#训练模型：
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(x_train,y_train)
#预测新样本：
x_new = np.array([[5,2.9,1,0.2]])
y_new = knn.predict(x_new)
print(iris_datasets['target_names'][y_new])
#计算精度
acc_test = knn.score(x_test,y_test)
print(acc_test)
acc_train = knn.score(x_train,y_train)
print(acc_train)

#精度随k值增大的变化情况：
acc_train_list = []
acc_test_list  = []
for i in range(10):
    knn = KNeighborsClassifier(n_neighbors = i+1)
    knn.fit(x_train,y_train)
    acc_train_list.append(knn.score(x_train,y_train))
    acc_test_list.append(knn.score(x_test,y_test))
#print(acc_train_list)
#print(acc_test_list)

# plt.plot([i+1 for i in range(10)],acc_train_list,label = 'train acc')
# plt.plot([i+1 for i in range(10)],acc_test_list ,label = 'test acc')
# plt.legend()
# plt.show()

from sklearn.datasets import load_breast_cancer

cancer_datasets = load_breast_cancer()

x_train,x_test,y_train,y_test = train_test_split(cancer_datasets.data,cancer_datasets.target,random_state=66,train_size=0.15)

print(x_train.shape)
print(y_train.shape)

k_numbers = [i+1 for i in range(10)]
cancer_acc_train_list = []
cancer_acc_test_list  = []
for i in range(10):
    knn_cancer = KNeighborsClassifier(k_numbers[i])
    knn_cancer.fit(x_train,y_train)
    cancer_acc_train_list.append(knn_cancer.score(x_train,y_train))
    cancer_acc_test_list.append(knn_cancer.score(x_test,y_test))

plt.plot(k_numbers,cancer_acc_train_list,label = 'train_acc')
plt.plot(k_numbers,cancer_acc_test_list,label='test_acc')
plt.legend()
plt.show()