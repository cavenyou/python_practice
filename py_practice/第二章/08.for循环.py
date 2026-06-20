#for循环框架
"""
for 元素 in 待处理数据集 :
    循环体代码(对元素进行处理)
else :
    循环结束后执行的代码
"""

#案例--------遍历字符串
#定义要遍历的字符串
# msg = "hello_python"
#
# #遍历字符串
# for i in msg:
#     print(i)
# else :
#     print("循环结束")
#
# print("---------------------\n")

#案例------------计算1---100之间所有奇数之和
#range语句用法:
"""
range(end) -> 获取一个从零开始到end结束的数字序列(不含end)
range(start,end) -> 获取一个从start开始到end结束的数字序列(不含end)
range(start,end,step) -> 获取一个从start开始到end结束的数字序列,步长是step(不含end) 
"""
# total1: int = 0
# for i in range(1,101):
#     if i % 2 != 0:
#         total1 += i
# print(f"1-100之间的奇数之和为:  {total1}")

#案例----------------计算100-500之间所有3的倍数的数字之和
total2: int = 0
for i in range(100,501):
    if i % 3 == 0:
        total2 += i
print(f"100-500之间所有3的倍数之和为{total2}")
