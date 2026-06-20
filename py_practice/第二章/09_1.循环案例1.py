"""
        案例: 根据输入的用户名密码执行登录操作,具体要求如下:
        1.正确的用户名和密码为admin/666888,zhangsan/123456,cavenyou/zxc000
        2.输入用户名和密码进行登录,直到登陆成功,程序结束运行;如果登录失败,则继续输入用户名和密码进行登录
        3.输入的用户名和密码不能为空!
        4.登陆成功: 输出"登陆成功!"
        5.登录失败: 输出"用户名或密码错误,还有-次机会,请重新输入!"
        6.五次机会,失败则锁定登录界面
"""
#存储正确的用户名和密码
right_account1 = "admin"
right_account2 = "zhangsan"
right_account3 = "cavenyou"
right_password1 = "666888"
right_password2 = "123456"
right_password3 = "zxc000"

#错误重试机会(5)
chance = 5

#循环条件定义
s = True
while s:
    # 输入账号和密码
    account = input("账号: ")
    password = input("密码: ")

    # 循环判定结果是否正确
    if account.strip() == "" or password.strip() == "": #strip是用来去空格的
        print("账号或密码不能为空,请重试")
    elif account == right_account1 and password == right_password1:
        print("登陆成功")
        s = False  #也可以用break来直接跳出循环
    elif account == right_account2 and password == right_password2:
        print("登陆成功")
        s = False
    elif account == right_account3 and password == right_password3:
        print("登陆成功")
        s = False
    else:
        chance -= 1
        if chance != 0:
            print(f"账号或密码错误,请重试!还有{chance}次机会")
        else:
            print("重试次数已耗尽,界面已锁定")
            s = False
