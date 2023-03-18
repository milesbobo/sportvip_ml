# #1.参数会改变原始的容器内容：
# def append_element(list, element):
#     list.append(element)
#     return list
#
# list1 = [1,2,3,4,5]
#
# print(append_element(list1,6))
#
# #2.isinstance 判断是否为实例。
# print(isinstance([1,2,3],list))
# print(isinstance([1,2,3],(dict,tuple)))
#
# #3.迭代方法
# def isiterable(object):
#     try:
#         iter(object)
#         return True
#     except TypeError:
#         return False
#
# print(isiterable([1,2,3,4]))
# print(isiterable('12345'))
#
# #4.变量的引用和新建对象
#
# list2 = [1,2,3,4,5]
# list3 = list2 * 2
# print(list3)
# print(id(list2))
# print(id(list3))
# list2 = [1,2,3,4,5,6]
# print(list2)
# print(list3)
# print(id(list2))
# print(id(list3))
#
# #5.字符串切片
# print("nihao"[2:4])
#
# #6.字符串格式化
# age = 28
# name = 'miles'
# print(f"My name is {name},My age is {age}")
# format_spec = "My name is {0:s},My age is {1:d}"
# print(format_spec.format(name,age))
#
# #7.循环+if语句。
# list_A = [1,2,3,None,4,None,5,6,7,None]
# for i in range(len(list_A)):
#     if(list_A[i]!=None):
#         print(f"The number is {list_A[i]}")
#     else:
#         print(f"It is None!")
#
# for i in list_A:#可迭代序列，不一定需要索引定位。
#     if(i!=None):
#         print(f"The number is {i}")
#     else:
#         continue
#         print(f"It is None!")

# #8.三元表达式。
# list_A = [1,2,3,4,5,6,7,8,9,10]
# list_B = [lambda i: i *2 for value in list_A]#列表推导式可以放lambda函数吗？-- 可以的
# list_C = list(map(lambda i:i*2,[value for value in list_A]))
# #lambda表达式和推导式的组合用法：
# # ① 先使用列表推导式，生成一个列表。
# # ② 使用map函数，把lambda函数作用于①生成的列表。
# # ③ map返回一个迭代器对象，必须使用list()接收，不能直接用[]。
# print(type(list_B))
# print(list_B)
# print(list_C)

# #9.元组(tuple)。
# tuple_A = 2,3,4
# print(type(tuple_A))
# string_A = "Hello world!"
# tuple_B = tuple(string_A)#tuple函数可以把任意序列或迭代器转化为元组。
# print(tuple_B)
# #9.1 元组拆包：
# tuple_A = ([1,2,3],[4,5,6],[7,8,9])
# for i,j,k in tuple_A:
#     print(f"a={i},b={j},c={k}")
# #9.2 元组方法,对元组中数据计数，并把个数作为value，值作为key生成字典。
# tuple_A = ('red','blue','red','red','yellow','green','blue','white','black','orange')
# set_A = set(tuple_A)
# dict_A = {key:value for key,value in zip([tuple_A.count(item) for item in set_A],list(set_A))}
# print(dict_A)#key不能重复。

# #10.列表（list）.
# #10.1 列表基本操作（增加元素，移除元素，修改元素，查找元素）
# list_A = [1,2,3,4,5]
# list_A.append(5)
# print(list_A)
# list_B = [6,7,8,9]
# list_A.extend(list_B)
# print(list_A)
# print(list_A.pop(-1))
# print(list_A)
# list_A.insert(1,100)
# print(list_A)
# list_A.sort()#sort是方法，改变自身对象；sorted是函数，生成副本。
# print(list_A)

#11. 内建序列函数。
# color = ['red','blue','yellow','orange','green','white','black']
# index = [0,1,2,3,4,5,6]
# dict_A = { key:value for key,value in enumerate(color) if value != 'white'}
# dict_B = { key:value for key,value in zip(index,color)}
# print(dict_B)

# #12.字典（dict）.
# color = ['red','blue','yellow','orange','green','white','black']
# index = [0,1,2,3,4,5,6]
# dict_A = { key:value for key,value in enumerate(color) if value != 'white'}
# print([i for i in dict_A.keys()])
# print([i for i in dict_A.values()])
# #字典的get方法和pop方法，对于不存在的键的处理。
# print(dict_A[1])
# print(dict_A.get(1))
# print(dict_A.get(100))
# print(dict_A.get(100,100))

#13.集合（Set）
#14.推导式：
# #15.函数，匿名函数
# list_A = [1,2,3,4,5]
# def map_fun(seq,f):
#     return [f for i in seq]
# list_B = map_fun(list_A,lambda i:i*2)
# print(list_B)

# #16.生成器:建一个对给定输入参数处理为平方的生成器
# def square_num(num = 10):
#     value = lambda x:x**2
#     list_N = list(map(value,[i for i in range(num)]))
#     yield list_N
#
# x = square_num()
# for i in square_num(10):
#     print(i)

#17. 异常和错误处理