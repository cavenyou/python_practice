"""
match 匹配变量
    case "匹配值"      "|表示或"
        ...
    ...
        ...
       .
       .
       .
    case _ ("_"代表其他)
"""
#案例---日志安排查询
#输入查询的星期
# day = input("请输入星期几(1--7): ")
# #进行模式匹配输出
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     case "4":
#         print("周四")
#     case "5":
#         print("周五")
#     case "6"|"7":
#         print("休息日")
#     case _:
#         print("输入错误!!!!!!!")

#简易计算器--------用户输入需要计算的两个数和运算符之后就可以进行计算
#输入数和运算符
num1 = float(input("请输入第一个字: "))
num2 = float(input("请输入第二个字: "))
operator = input("请输入运算符(+ - * /): ")

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 + num2)
    case "*":
        print(num1 * num2)
    case "/" if num2 != 0 :#满足if条件之后才继续进行匹配
        print(num1 / num2)
    case _ :
        print("输入错误啦啦啦!")