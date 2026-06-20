"""
    案例: 猜数字游戏
    1. 系统随机生成一个随机数
    2. 用户根据提示猜数字,并将所猜的数字输入系统
    3. 如果猜错,系统给出提示是猜大了,还是猜小了,然后继续输入猜的数字
    4. 如果猜对,系统自动退出,游戏结束
"""
import random
random_number = random.randint(1,100)
gauss = int(input("请输入你的猜测值: "))
while True:
    if gauss == random_number:
        print("恭喜你猜对了!")
        break
    elif gauss > random_number :
        gauss = int(input("猜大了,请重新输入: "))
    else:
        gauss = int(input("猜小了,请重新输入: "))
print(f"随机生成的数字是{random_number}")
