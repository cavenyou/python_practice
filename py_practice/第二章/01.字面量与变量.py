# 字面量的写法
print(100)
print(3.14)
print(True) #首字母大写
print(False) #bool类型本质是整数0 1
print("Hello Python")
print("----------------------------")
print(None) #空值(NoneType)

#变量 python是动态类型语言 一个变量可以存储不同类型的变量
num = 1650
print(num)

num = num + 1
print(num)

#案例
base = 20.7 #基础播放量
incr = 50   #新增播放量
print("未来第一个月的播放总量",base + incr)
print("未来第二个月的播放总量",base + 2*incr)

#一次定义多个变量
base,incr = 20.7,50
print("未来第一个月的播放总量",base + incr)
print("未来第二个月的播放总量",base + 2*incr)


#标识符命名（变量、函数、类等元素名）规则
# 1 英文 数字 下划线（_）
# 2 不能数字开头
# 3 大小写有区分
# 4 不能使用关键字

# 变量名命名规范
# 1 见名知意
# 2 多部分用下划线连接
# 3 英文用小写


# 案例 交换a、b的值，并输出
a = 10
b = 20

c = a
a = b
b = c
print(a)
print(b)

# 练习 a b c 交换为 c a b
a = 100
b = 200
c = 300 #赋值

mid1 = a
a = b
b = c
c = mid1
print(a)
print(b)
print(c)
