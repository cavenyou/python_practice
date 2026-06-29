"""
    set:    无序的,不可重复的,可修改的数据容器
    定义:set1 = {"A","B","C","D","E","F","G","H","I"}
    空集合: set2 = set()
"""

s = {1, "A", 2, "B",1,2,"A","A"}
print(s)
print(type(s))

"""
    集合常用方法: 
    add(..): 添加元素  s1.add('t')
    remove(..): 删除集合中的指定元素(若元素不存在则会报错)  s1.remove('t')
    pop(): 随机删除集合中的元素并返回  s1.pop()
    clear(): 清空集合  s1.clear()
    difference(): 求取两个集合的差集   s1.difference(s2) : 在s1而不再s2中的元素集合
    union(): 求取两个元素的并集  s1.union(s2)
    intersection(): 求取两个元素的交集  s1.intersection(s2)
"""

s1 = {199,299,399,123,1234}
print(s1)

#sdd()
s1.add(200)
print(s1)

#remove()
s1.remove(123)
print(s1)

#pop()
s1.pop()
print(s1)

#clear()
s1.clear()
print(s1)



s2 = {1,2,3,4,5,6,7,8,9}
s3 = {4,6,7,8,9,10,11,12,13}

#difference()
s2.difference(s3)
print(s2)

#union()
s2.union(s3)
print(s2)

#intersection()
s2.intersection(s3)
print(s2)

#从代码运行结果可发现s2并未被修改,这是因为后面三个方法是返回一个新的集合,而不是说修改s2
print(s2.difference(s3))
print(s2.union(s3))
print(s2.intersection(s3))