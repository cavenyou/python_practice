#案例1-----将用户输入的十个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值,最大值和平均值
#定义列表
# s = []
# total = 0
# for i in range(1,11):
#     s.append(int(input(f"请输入第{i}个数字:  ")))
#     total += s[-1]#或者用sum(s)
# print(s)
# s.sort()
# print(f'最小值是{s[0]}')    #min()--获取最小值
# print(f'最大值是{s[-1]}')   #max()--获取最大值
# average = total / len(s)    #len()--获取列表的长度
# print(f'平均值是{average}')


print("-------------------------------------------------------------------------")
#案例2-----------合并两个列表中的元素,并对合并的结果进行去重处理
#定义列表
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# #合并列表
# num_list_total = [*num_list1,*num_list2]    #或者用num_list1+num_list2
# num_list_new = []
# print(num_list_total)
#
# for num in num_list_total:
#     if num in num_list_new:
#         print(num)
#     else :
#         num_list_new.append(num)
# print (num_list_new)
# num_list_new.sort()
# print(num_list_new)


print("--------------------------------------")
"""
    案例3: 1.生成1--20的平方列表
          2.从如下数字列表中提取所有偶数,并计算其平方,组成一个新的列表
"""
num_square_list = []
#方式一
for i in range(1,21):
    num_square_list.append(i**2)
print(num_square_list)
#方式二 : 列表推导式-------按照一定的规则快速生成一个列表的方法 --> 格式: [要插入的值 for i in 序列/列表 if条件]
# num_square_list = [i**2 for i in range(1,21)]
num_new_square_list = [i**2 for i in num_square_list if i%2==0]
print(num_new_square_list)