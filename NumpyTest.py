import numpy as np

list_A = [1,2,3,4,5]
array_A = np.array(list_A)
print(array_A)

list_B = [[1,2,3,4],[5,6,7,8]]
array_B = np.array(list_B)
print(array_B)
print(array_B.shape)
print(array_B.dtype)

list_A = ([1,2,3,4],[5,6,7,8])
array_A = np.array(list_A)
print(array_A)

set_A = {1,2,3,4,5}
array_A = np.array(set_A)
print(array_A)
print(type(array_A))

#快速生成ndarray方法：
print(np.ones((2,2)))
print(np.zeros((2,2)))

#布尔索引
colors = np.array(['red','bule','green','yellow','orange'])
numbers = np.random.randn(5,10)
print(numbers)
print(colors == 'red')
print(numbers[colors == "red"])#本质是传入一个布尔类型的数组。

#通用函数
