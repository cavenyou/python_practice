#元组: 可重复,有序,不可修改

#元组定义
tup = (1,2,3,4,5,6,7,8,9)

#索引(正反均可)
print(tup[0])
print(tup[-1])

#切片
print(tup[0:9:2])
print(tup[::-1])

#索引查询
print(tup.index(4))

#count():统计元素个数
print(tup.count(4))

#注意: 定义单个元素的元组时,需要在后面加上一个逗号
tup_simple = (1,)
print(type(tup_simple)) #tuple
tup_simple = (1)
print(type(tup_simple)) #int


#元组的组包与解包
# 组包
t1 = (1,2,3,4,5,6,7,8,9)
t2 = 1,2,3,4,5,6,7,8,9
print(t1)
print(t2)

#基础解包
a,b,c,d,e,f,g,h,i = t1
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

#进阶解包
first,*other = t1
print(first)
print(*other)

first,*other,last = t1
print(first)
print(*other)
print(last)

*other,last = t1
print(*other)
print(last)

#案例: 将a,b,c的值调换为c,a,b
a = 1
b = 2
c = 3

c,a,b = a,b,c
print(a)
print(b)
print(c)