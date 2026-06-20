#定义列表
s = [178,18982,"python","zephyr",True]

print(type(s))
print(s[-5])    # 反向索引,最后一个元素从-1开始
print([0])      # 正向索引,第一个元素从0开始

print("------------------------------------")
 #修改
s[0] = "已修改"
print(s[0])

#删除
del s[2]
print(s)

#遍历
for item in s:
    print(item)