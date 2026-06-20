#if条件判断,如果分数超过690,我就去清华
score = 698
if score > 690 :#不要丢冒号
    print ("欢迎你来清华读书")
print("-----------------------------")#不属于if代码块的语句(前方无缩进)

# # 案例1. 模仿B站登录功能的实现(正确的账号/密码:18888888888/666888)
# #正确账号和密码
# right_account = "18888888888"
# right_password = "666888"
#
# #输入账号和密码
# account = input("请输入您的账号: ")
# password = input("请输入您的密码: ")
#
# #如果账号密码正确,则进入主页
# if account == right_account and password == right_password:
#     print("登陆成功")
#     print("进入主页")
#
# #如果错误则登录失败,提示错误信息
# else:
#     print("登录失败")
#     print("账号或密码错误")

# #案例2. 根据用户输入的年份,判断这一年是闰年还是平年
# year = int(input("请输入年份: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print(f"{year}年是闰年")
# else :
#     print(f"{year}年是平年")

#案例3. 判断一个数字是正数/负数/0
# num = int(input("请输入想要判断的数: "))
#
# if num > 0 :
#     print(f"{num}是正数")
#
# elif num < 0 :
#     print(f"{num}是负数")
#
# else :
#     print(f"{num}是0")


#案例4. 继续登录板块的设计,这次是三组
#用户名/密码为  admin/666888  root/547527  zhangsan/123456
#否则就提示用户名或密码错误

#记录正确账号密码
# right_account_1 = "admin"
# right_password_1 = "666888"
#
# right_account_2 = "root"
# right_password_2 = "547527"
#
# right_account_3 = "zhangsan"
# right_password_3 = "123456"
#
# #输入账号和密码
# account = input("请输入您的账号: ")
# password = input("请输入您的密码: ")
#
# #判断账号密码是否正确
# if account == right_account_1 and password == right_password_1:
#     print("登陆成功!")
# elif account == right_account_2 and password == right_password_2:
#     print("登陆成功")
# elif account == right_account_3 and password == right_password_3:
#     print("登陆成功")
# else :
#     print("登陆失败")
#     print("用户名或密码错误")


#案例5. 判断三角形类型
"""
三角形判定: 两边之和大于第三边
等边三角形: 三边相等
等腰三角形: 有两边相等
普通三角形
不能构成三角形
"""

#输入三角形三条边
# a = int(input("请输入第一条边的长度: "))
# b = int(input("请输入第二条边的长度: "))
# c = int(input("请输入第三条边的长度: "))
#
# if not((a + b > c ) and (c + a > b) and (c + b > a)) : #判断是否为三角形
#     print("这三条边不能构成三角形")
# elif a == b ==c :
#     print("该三角形为等边三角形")
# elif a == c or b == c or a == b :
#     print ("该三角形为等腰三角形")
# else :
#     print("该三角形为普通三角形")


# 案例6. 电费计算
"""
分段定价,阶梯状逐级递增
第一档: 2880度以下,电费单价0.4883/度
第二档: 2880-4800度以下,电费单价0.5383/度
第一档: 4800度以下,电费单价0.7883/度
"""

#键入用电量
ele_consumption = float(input ("请输入您的用电量（单位：度）： "))

#判断档级,计算电费
if ele_consumption <= 2880 :
    print(f"{ele_consumption}度所用电费为{0.4883* ele_consumption}元")
elif 2880 < ele_consumption <= 4800 :
    print(f"{ele_consumption}度所用电费为{0.5383 * (ele_consumption - 2880) + 2880*0.4883}元")
else :
    print(f"{ele_consumption}度所用电费为{0.7883 * (ele_consumption - 4800) + (4800-2880)*0.5383 + 2880 * 0.4883}元")
