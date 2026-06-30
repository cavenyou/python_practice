"""

    函数定义:
def 函数名(参数列表):
    函数体
    .....
    return 返回值

调用函数:
函数名(参数)

"""

def line():
    print("------------------------------")

#函数调用
line()
line()
line()
line()
line()
line()

#参数与返回值

#计算长方形的面积
def rectangle_area(l,w):
    area = l * w
    return area

rectangle_area = rectangle_area(5,5)
print(rectangle_area)

#计算圆的面积和周长
def circle_area_perimeter(r):
    """
    该函数用来计算圆的面积和周长
    :param r: 圆的半径
    :return: 圆的面积,圆的周长
    """
    area = 3.14 * r * r
    perimeter = 2 * r * 3.14
    return area, perimeter # 是可以返回多个值的,多个返回值之间用逗号分割

al = circle_area_perimeter(10)
print(al)
print(type(al)) #多个返回值会自动封装到元组之中


#函数的嵌套调用: 在一个函数中又调用了另外一个函数  遵循后进先出 pass
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()


#案例
"""
    1.定义一个函数: 根据传入的底和高计算三角形的面积
    2.定义一个函数: 计算传入的字符串中元音字母的个数(aeiouAEIOU)
    3.定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分,最低分,平均分(保留1位小数),并返回
"""
#计算三角形面积
def triangle_area(b,h):
    """
    这个函数用来计算三角形面积
    :param b: 三角形的底
    :param h: 三角形的高
    :return: 三角形面积
    """
    area = b * h / 2
    return area

#计算元音字母的个数
def vowel_num(text):
    """
    这是一个计算字符串中元音字母个数的函数
    :param text: 将要计算的字符串
    :return: 元音个数
    """
    num = (text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u') +
           text.count('A') + text.count('E') + text.count('I') + text.count('O') + text.count('U'))
    return num

#计算班级学员高考成绩最高/低分和平均分
def calc_score(score_list):
    """
    函数用来计算一段成绩的最高分,最低分,平均分
    :param score_list: 成绩列表
    :return: 最高分,最低分,平均分
    """
    s_max = max(score_list)
    s_min = min(score_list)
    s_average = sum(score_list)/len(score_list)
    return s_max, s_min, s_average

#三角形参数输入
bottom = float(input("请输入三角形的底"))
high = float(input("请输入三角形的高"))
triangle_area = triangle_area(bottom,high)
print(f"三角形的面积为{triangle_area:.1f}")

#字符串输入
test = input("请输入要检测的字符串:")
num = vowel_num(test)
print(f"字符串{test}中共有{num}个元音字母")

#成绩输入
user_input = input("请输入成绩单,不同成绩用逗号隔开:")
score_list = [int(i) for i in user_input.split(",")]
s_max, s_min, s_average = calc_score(score_list)
print(f"学员中最高分为{s_max}分,最低分为{s_min}分,平均分是{s_average:.1f}分")