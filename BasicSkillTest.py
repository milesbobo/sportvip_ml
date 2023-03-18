
#1.参数会改变原始的容器内容：
def append_element(list, element):
    list.append(element)
    return list

list1 = [1,2,3,4,5]

print(append_element(list1,6))

#2.isinstance 判断是否为实例。
print(isinstance([1,2,3],list))
print(isinstance([1,2,3],(dict,tuple)))

#3.迭代方法
def isiterable(object):
    try:
        iter(object)
        return True
    except TypeError:
        return False

print(isiterable([1,2,3,4]))
print(isiterable('12345'))

#4.变量的引用和新建对象

list2 = [1,2,3,4,5]
list3 = list2 * 2
print(list3)
print(id(list2))
print(id(list3))
list2 = [1,2,3,4,5,6]
print(list2)
print(list3)
print(id(list2))
print(id(list3))

#5.字符串切片
print("nihao"[2:4])

#6.字符串格式化
age = 28
name = 'miles'
print(f"My name is {name},My age is {age}")
format_spec = "My name is {0:s},My age is {1:d}"
print(format_spec.format(name,age))

#7.