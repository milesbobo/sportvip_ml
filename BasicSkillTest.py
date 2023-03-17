
#参数会改变原始的容器内容：

def append_element(list, element):
    list.append(element)
    return list

list1 = [1,2,3,4,5]

print(append_element(list1,6))

#