"""
    字符串: 字符的容器
    特点: 不可修改,有序性,可迭代性
    每一个元素都有相对应的索引(正向/反向索引)
"""
str = "hello-cavenyou"

for c in str:
    print(c,end=" ")
print()
#切片:切片操作与list列表语法一致
print(str)
print(str[0:-1:2])  #步长为正数代表从前往后截取
print(str[-1:0:-2]) #步长为负数代表从后往前截取
print(str[::-1])    #反转字符串