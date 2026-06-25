"""
    append()    在列表的尾部追加元素                           样例:s.append(18297)
    insert()    在指定索引之前,插入该元素                       样例:s.insert(0,18297)--在0前插入元素18297
    remove()    移除列表中第一个匹配到的值                      样例:s.remove(7)--删除对应值,第一个对应的
    pop()       删除列表中指定索引位置的元素(未指定则最后一个)      样例:s.pop()--删除索引处元素
    sort()      对列表进行排序(需要列表数据的类型一致)            样例:s.sort()
    reverse()   反转列表元素                                 样例:s.reverse()
"""

# 案例
s = [0,39,1,4,2,4,5,6,7,8,"neeed_del",9]

s.append(10)
print(s)
print("--------------------")

s.insert(4,3)
print(s)
print("--------------------")

s.remove(4)
print(s)
print("--------------------")

s.pop(-3)
print(s)
print("--------------------")

s.sort()
print(s)
print("--------------------")

s.reverse()
print(s)